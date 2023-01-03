import dramatiq
from periodiq import cron


@dramatiq.actor(periodic=cron('*/10 * * * *'))
def recalculate_movie_rating():
    # TODO: Run as sync code
    # await session.execute(
    #     update(
    #         Movie
    #     ).values(
    #         rating=bindparam('average_rating')
    #     ).where(
    #         Movie.id == bindparam('movie_id')
    #     ),
    #     [
    #         {'movie_id': result.id, 'average_rating': result.avg}
    #         for result in (session.execute(
    #         select(
    #             Movie.id, func.avg(Rating.score)
    #         ).select_from(
    #             Movie
    #         ).join(
    #             Rating
    #         ).group_by(
    #             Movie.id
    #         )
    #     )).fetchall()
    #     ]
    # )
    # await session.commit()

    pass
