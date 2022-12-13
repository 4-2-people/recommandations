from fastapi import Depends
from fastapi.security import HTTPBasicCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from apps.user.exceptions import UserNotFoundError, UserCredentialsError
from settings import security
from database import get_session
from apps.user.models import User


async def get_current_user(
    session: AsyncSession = Depends(get_session),
    credentials: HTTPBasicCredentials = Depends(security)
) -> User:
    user = (
        await session.execute(
            select(User).where(User.username == credentials.username)
        )
    ).scalar_one_or_none()

    if not user:
        raise UserNotFoundError()

    if not User.verify_password(credentials.password, user.password):
        raise UserCredentialsError()

    return user
