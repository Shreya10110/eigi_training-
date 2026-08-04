# routes/auth_routes.py
from fastapi import APIRouter, Depends, status
from odmantic import AIOEngine

from config.database import get_engine
from requests.user_requests import SignupRequest, LoginRequest, ResetPasswordRequest, GenericResponse, LoginResponse
from controllers import auth_controllers

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/signup", response_model=GenericResponse, status_code=status.HTTP_201_CREATED)
async def signup(request: SignupRequest, engine: AIOEngine = Depends(get_engine)):
    """Signup endpoint - Registers a new user."""
    return await auth_controllers.signup_controller(request, engine)

@router.post("/login", response_model=LoginResponse, status_code=status.HTTP_200_OK)
async def login(request: LoginRequest, engine: AIOEngine = Depends(get_engine)):
    """Login endpoint - Authenticates user and returns JWT token."""
    return await auth_controllers.login_controller(request, engine)

@router.post("/reset-password", response_model=GenericResponse, status_code=status.HTTP_200_OK)
async def reset_password(request: ResetPasswordRequest, engine: AIOEngine = Depends(get_engine)):
    """Reset Password endpoint - Updates user password."""
    return await auth_controllers.reset_password_controller(request, engine)
