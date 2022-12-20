from sqlalchemy import Column, String, ForeignKey, Integer, Float, UniqueConstraint
from sqlalchemy.orm import relationship, validates

from apps.movie.exceptions import InvalidScoreError
from database import Model


class Movie(Model):
    """Model representing the movie object."""

    title = Column(String(64), nullable=False)
    description = Column(String(1024))
    rating = Column(Float, nullable=False, default=0)


class Rating(Model):
    """The rating given to the movie by the user."""

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', foreign_keys=[user_id])
    movie_id = Column(Integer, ForeignKey('movie.id'), nullable=False)
    movie = relationship('Movie', foreign_keys=[movie_id])
    score = Column(Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint('user_id', 'movie_id'),
    )

    @validates('score')
    def validate_score(self, field: str, score: int) -> int:
        if 10 <= score < 0:
            raise InvalidScoreError()

        return score
