from pydantic import BaseModel
from enum import Enum

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None
    scopes: list[str] = []

class Role(str, Enum):
    admin = "admin"
    patient = "patient"
    doctor = "doctor"

class Auth(BaseModel):
    id: str
    hashed_password: str
    role: Role
    user_id: str

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None

class UserInDB(User):
    id: str
