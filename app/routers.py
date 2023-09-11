from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from typing import Annotated
from fastapi import Depends, HTTPException
from .schemas import User, Auth, Token
from .dependencies import get_current_user, validate_role, authenticate_user, create_access_token
from .constants import ACCESS_TOKEN_EXPIRE_MINUTES
from .db import fake_users_db, auth_db, permissions_db


router = APIRouter()

@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user, user_auth = authenticate_user(fake_users_db, auth_db, form_data.username, form_data.password)
    if not user or not user_auth:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.id, "scopes": [user_auth.role.value]},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/status/")
async def read_system_status(current_user: Annotated[User, Depends(get_current_user)]):
    return {"status": "ok"}


# confirm auth for path and method
@router.get("/auth/{url_path:path}")
async def read_auth(
    current_user: Annotated[Auth, Depends(get_current_user)],
    method: str,
    url_path: str,
):
    if not await validate_role(permissions_db, current_user, url_path, method):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return True