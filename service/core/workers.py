from settings import *
from apps.movie.tasks import recalculate_movie_rating


@dramatiq.actor
def worker():
    print('test worker')
