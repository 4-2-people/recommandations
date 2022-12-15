from periodiq import cron

from settings import *


@dramatiq.actor
def worker():
    print('test worker')


@dramatiq.actor(periodic=cron('* * * * *'))
def every_minute():
    print('test schedule task')
