from pydantic import BaseModel
from pydantic.types import constr

from .models import User


class UserBase(BaseModel):
    username: constr(strip_whitespace=True, max_length=User.username.type.length)
    email: constr(strip_whitespace=True, max_length=User.email.type.length)

    class Config:
        orm_mode = True


class UserSignUp(UserBase):
    password: constr(strip_whitespace=True, max_length=User.password.type.length)


class UserProfile(UserBase):
    pass
