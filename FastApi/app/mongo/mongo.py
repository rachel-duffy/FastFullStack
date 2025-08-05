from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from app.movie import movie

uri = ""

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
movie_db = client.movie_db
movie_collection = movie_db["movies"]


async def get_movies():
    return movie_collection.find({}, {'_id': 0})


async def post_movie(new_movie: movie.Movie):
    movie_dict = new_movie.model_dump()
    return movie_collection.insert_one(movie_dict)

async def delete_movie(movie_name: str):
    movie_collection.delete_one({"name" : movie_name})
