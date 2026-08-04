# models/user_models.py
from __future__ import annotations
from datetime import datetime
from odmantic import Model

class User(Model):
    name: str
    email: str
    password: str
    created_at: datetime
