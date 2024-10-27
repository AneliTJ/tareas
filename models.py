from sqlmodel import SQLModel, Field

class MoviesModel(SQLModel, table =True):
    __tablename__ = "movies"

    id: int = Field(primary_key=True)
    name: str
    year: int
    duration: str
    director: str
    classification: str
    genre: str

