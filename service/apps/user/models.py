import email_validator
from sqlalchemy import Column, String, UniqueConstraint
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import validates

from database import Model
from settings import password_context
from .exceptions import UserAlreadyExists


class User(Model):
    """Model of the user registered in the system."""

    username = Column(String(64), nullable=False)
    email = Column(String(256), nullable=False)
    password = Column(String(128), nullable=False)

    __table_args__ = (
        UniqueConstraint('username', 'email'),
    )

    @validates('email')
    def validate_email(self, field: str, address: str) -> str:
        return email_validator.validate_email(
            address, check_deliverability=True
        ).email

    @validates('password')
    def validate_password(self, field: str, password: str) -> str:
        return password_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return password_context.verify(plain_password, hashed_password)

    @staticmethod
    async def create(
        session: AsyncSession, username: str, email: str, password: str
    ):
        try:
            async with session.begin():
                session.add(
                    User(username=username, email=email, password=password)
                )
                await session.commit()
        except IntegrityError:
            raise UserAlreadyExists()
