from pydantic import BaseModel
from pydantic.types import constr

from .models import Movie


class MovieBase(BaseModel):
    id: int
    title: constr(max_length=Movie.title.type.length)
    description: constr(max_length=Movie.description.type.length)
    rating: float

    class Config:
        orm_mode = True


class MovieItem(MovieBase):
    pass
