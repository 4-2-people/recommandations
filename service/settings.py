import dramatiq
from dramatiq.brokers.redis import RedisBroker
from periodiq import PeriodiqMiddleware
from dramatiq.middleware import default_middleware
from fastapi.security import HTTPBasic
from passlib.context import CryptContext


class Cache:
    HOST = 'cache'
    PORT = 6379

    @classmethod
    def url(cls) -> str:
        return f'redis://{cls.HOST}:{cls.PORT}'

    @classmethod
    def worker_queue(cls) -> str:
        return f'{cls.url()}/0'


DATABASE_URL = 'postgresql+asyncpg://user:password@database:5432/database'

# FastApi specific settings
security = HTTPBasic()
password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

# Setup asynchronous workers with a Redis broker
broker = RedisBroker(
    url=Cache.worker_queue(),
    # Disable prometheus middleware
    middleware=[m() for m in default_middleware[1:]]
)
broker.add_middleware(PeriodiqMiddleware(skip_delay=30))
dramatiq.set_broker(broker)
