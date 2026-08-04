# requests/user_requests.py
from pydantic import BaseModel
from typing import Optional, Dict, Any

class SignupRequest(BaseModel):
    name: str
    email: str
    password: str

class LoginRequest(BaseModel):
    email: str
    password: str

class ResetPasswordRequest(BaseModel):
    email: str
    new_password: str
    otp: Optional[str] = None

class GenericResponse(BaseModel):
    status: bool = True
    message: str
    data: Optional[Dict[str, Any]] = None

class LoginResponse(BaseModel):
    status: bool = True
    message: str
    access_token: str
    token_type: str = "bearer"
