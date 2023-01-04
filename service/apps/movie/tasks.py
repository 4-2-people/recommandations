import asyncio

import dramatiq
from periodiq import cron
from sqlalchemy import update, bindparam, select, func

from apps.movie.models import Movie, Rating
from database import Session


@dramatiq.actor(periodic=cron('*/10 * * * *'))
def recalculate_movie_rating():
    async def update_rating():
        async with Session() as session:
            await session.execute(
                update(
                    Movie
                ).values(
                    rating=bindparam('average_rating')
                ).where(
                    Movie.id == bindparam('movie_id')
                ),
                [
                    {'movie_id': result.id, 'average_rating': result.avg}
                    for result in (await session.execute(
                        select(
                            Movie.id, func.avg(Rating.score)
                        ).select_from(
                            Movie
                        ).join(
                            Rating
                        ).group_by(
                            Movie.id
                        )
                    )).fetchall()
                ]
            )
            await session.commit()

    asyncio.run(update_rating())
