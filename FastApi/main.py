from fastapi import FastAPI
from app.routers import movie
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:3001"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/heartbeat", tags=["Health"])
async def health():
    return {"message": "I'm alive"}

app.include_router(movie.router)
