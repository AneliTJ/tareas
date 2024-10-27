from pydantic import BaseModel

class MovieSchema (BaseModel):
    name: str
    year: int
    duration: str
    director: str
    classification: str
    genre: str

