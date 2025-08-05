from fastapi import APIRouter, HTTPException
from app.movie import movie
from app.mongo import mongo

router = APIRouter(
    prefix="/movie",
    tags=["movie"]
)


@router.get("/")
async def get_all_movies():
    all_movies = await mongo.get_movies()
    return list(all_movies)


@router.post("/")
async def post_movie(new_movie: movie.Movie):
    try:
        movie_inserted = await mongo.post_movie(new_movie)
        return {"message": "Movie inserted successfully", "inserted_id": str(movie_inserted.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to add movie: {new_movie.name}")

@router.delete("/")
async def delete_move(movie_name: str):
        try:
            await mongo.delete_movie(movie_name)
            return {"message": f"{movie_name} deleted successfully "}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to delete movie: {movie_name}")
