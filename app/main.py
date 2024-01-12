from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from app.database import User, Post
from app.config import getSettings
from app.routers import auth, post, user


app = FastAPI()

origins = [
    getSettings().CLIENT_ORIGIN
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, tags=['Auth'], prefix="/api/auth")
app.include_router(user.router, tags=['User'], prefix="/api/user")

@app.get("/")
async def index():
    return {"Message": "Welcome to CrudApi App.."}

