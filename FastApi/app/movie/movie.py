from pydantic import BaseModel


class Movie(BaseModel):
    name: str
    genre: str
    minutes_long: int
    year_released: int
