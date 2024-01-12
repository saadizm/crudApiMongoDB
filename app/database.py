import pymongo
from pymongo import MongoClient
from app.config import getSettings

settings = getSettings()

try:
    client = MongoClient(settings.DATABASE_URL)
    print("Connected to MongoDB....")
    print(f"Settings is ->{settings.DATABASE_URL}")
except Exception as e:
    print(f"Unable to connect to Database: Error cause by -> {str(e)}")


db = client[settings.MONGODB_NAME]
User = db.users
Post = db.posts
User.create_index([("email", pymongo.ASCENDING)], unique=True)
Post.create_index([("title", pymongo.ASCENDING)], unique=True)

