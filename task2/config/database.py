import os
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "user_db")

client = AsyncIOMotorClient(MONGO_URL)
engine = AIOEngine(client=client, database=DB_NAME)

def get_engine() -> AIOEngine:
    return engine
