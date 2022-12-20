from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from apps.auth.depends import get_current_user
from apps.user.models import User
from apps.movie.models import Movie
from apps.movie.schemas import MovieItem
from database import get_session


router = APIRouter()


@router.get('', response_model=list[MovieItem])
async def trends(
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session)
):
    movies = (
        await session.execute(select(Movie))
    ).scalars()

    return [MovieItem.from_orm(movie) for movie in movies]
