# crud/user_curd.py
from datetime import datetime, timezone
from typing import Optional
from odmantic import AIOEngine
from models.user_models import User

async def get_user_by_email(engine: AIOEngine, email: str) -> Optional[User]:
    """Find a user in MongoDB by their email address."""
    return await engine.find_one(User, User.email == email)

async def create_user(engine: AIOEngine, name: str, email: str, hashed_password: str) -> User:
    """Insert a new user record into MongoDB."""
    user = User(
        name=name,
        email=email,
        password=hashed_password,
        created_at=datetime.now(timezone.utc)
    )
    return await engine.save(user)

async def update_user_password(engine: AIOEngine, email: str, new_hashed_password: str) -> Optional[User]:
    """Update user's password in MongoDB."""
    user = await engine.find_one(User, User.email == email)
    if user:
        user.password = new_hashed_password
        await engine.save(user)
        return user
    return None

async def delete_user_by_email(engine: AIOEngine, email: str) -> bool:
    """Delete a user record from MongoDB by email."""
    user = await engine.find_one(User, User.email == email)
    if user:
        await engine.delete(user)
        return True
    return False
