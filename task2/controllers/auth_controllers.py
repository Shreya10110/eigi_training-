# controllers/auth_controllers.py
from fastapi import HTTPException, status
from odmantic import AIOEngine

from requests.user_requests import SignupRequest, LoginRequest, ResetPasswordRequest, GenericResponse, LoginResponse
from crud import user_curd
from utils import passwords, jwt_handler
from constants import message

async def signup_controller(request: SignupRequest, engine: AIOEngine) -> GenericResponse:
    """Business logic for User Signup."""
    # 1. Check if email already exists
    existing_user = await user_curd.get_user_by_email(engine, request.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message.USER_EXISTS
        )

    # 2. Hash password
    hashed_pwd = passwords.hash_password(request.password)

    # 3. Save user to MongoDB
    new_user = await user_curd.create_user(
        engine,
        name=request.name,
        email=request.email,
        hashed_password=hashed_pwd
    )

    # 4. Prepare response
    return GenericResponse(
        status=True,
        message=message.USER_CREATED,
        data={
            "id": str(new_user.id),
            "name": new_user.name,
            "email": new_user.email
        }
    )

async def login_controller(request: LoginRequest, engine: AIOEngine) -> LoginResponse:
    """Business logic for User Login."""
    # 1. Find user by email
    user = await user_curd.get_user_by_email(engine, request.email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message.INVALID_CREDENTIALS
        )

    # 2. Verify password
    if not passwords.verify_password(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message.INVALID_CREDENTIALS
        )

    # 3. Generate JWT Token
    access_token = jwt_handler.create_access_token(
        data={"sub": user.email, "id": str(user.id)}
    )

    # 4. Return token response
    return LoginResponse(
        status=True,
        message=message.LOGIN_SUCCESS,
        access_token=access_token,
        token_type="bearer"
    )

async def reset_password_controller(request: ResetPasswordRequest, engine: AIOEngine) -> GenericResponse:
    """Business logic for Reset Password (simple flow)."""
    # 1. Find user by email
    user = await user_curd.get_user_by_email(engine, request.email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=message.USER_NOT_FOUND
        )

    # 2. Hash new password
    new_hashed_pwd = passwords.hash_password(request.new_password)

    # 3. Update password in MongoDB
    await user_curd.update_user_password(engine, request.email, new_hashed_pwd)

    # 4. Return success response
    return GenericResponse(
        status=True,
        message=message.PASSWORD_RESET_SUCCESS
    )
