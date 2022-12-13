from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from apps.auth.depends import get_current_user
from apps.user.models import User
from apps.user.schemas import UserSignUp, UserProfile
from database import get_session

router = APIRouter()


@router.post('/sign-up', status_code=201)
async def sign_up(body: UserSignUp, session: AsyncSession = Depends(get_session)):
    await User.create(
        session=session, username=body.username, email=body.email, password=body.password
    )

    return {'detail': 'User successfully created'}


@router.get('/current', status_code=200, response_model=UserProfile)
async def current(user: User = Depends(get_current_user)):
    return UserProfile.from_orm(user)
