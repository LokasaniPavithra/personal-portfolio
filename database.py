from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)

db = client["portfolio_db"]

contacts = db["contacts"]

print("MongoDB Connected Successfully")