import dramatiq
from periodiq import cron


@dramatiq.actor(periodic=cron('*/10 * * * *'))
def recalculate_movie_rating():
    pass
