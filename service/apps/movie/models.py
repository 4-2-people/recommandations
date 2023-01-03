from sqlalchemy import (
    Column, String, ForeignKey, Integer, Float, UniqueConstraint, select, func
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import relationship, validates

from apps.movie.exceptions import InvalidScoreError
from database import Model


class Movie(Model):
    """Model representing the movie object."""

    title = Column(String(64), nullable=False)
    description = Column(String(1024))
    rating = Column(Float, nullable=False, default=0)

    @staticmethod
    async def top(session: AsyncSession, limit: int = 64) -> list[int]:
        """Get a list of the most popular movies by scores count and rating."""

        return (
            await session.execute(
                select(
                    Movie.id
                ).select_from(
                    Movie
                ).join(
                    Rating
                ).order_by(
                    Movie.rating.desc(),
                    func.count(Movie.scores).desc()
                ).group_by(
                    Movie.id
                ).limit(limit)
            )
        ).scalars()


class Rating(Model):
    """The rating given to the movie by the user."""

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', foreign_keys=[user_id], backref='scores')
    movie_id = Column(Integer, ForeignKey('movie.id'), nullable=False)
    movie = relationship('Movie', foreign_keys=[movie_id], backref='scores')
    score = Column(Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint('user_id', 'movie_id'),
    )

    @validates('score')
    def validate_score(self, field: str, score: int) -> int:
        if 10 <= score < 0:
            raise InvalidScoreError()

        return score
