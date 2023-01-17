import re
import datetime

from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

import settings

engine = create_async_engine(settings.DATABASE_URL, poolclass=NullPool)
Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()


async def get_session() -> AsyncSession:
    async with Session() as session:
        yield session


class Model(Base):
    __abstract__ = True

    id = Column(
        Integer,
        primary_key=True
    )
    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.datetime.now
    )
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now
    )

    @declared_attr
    def __tablename__(cls) -> str:
        return re.sub('(?!^)([A-Z]+)', r'_\1', cls.__name__).lower()
