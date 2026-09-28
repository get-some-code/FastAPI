from fastapi import FastAPI, HTTPException, status
from fastapi.responses import FileResponse
from pydantic import BaseModel

from jwt_test import create_access_token

from pwdlib import PasswordHash

app = FastAPI()

password_hash = PasswordHash.recommended()

users = {}

class UserRegister(BaseModel):
    name: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

@app.get("/")
def home():
    return FileResponse("index.html")


@app.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: UserRegister):

    stored_hashed_password = password_hash.hash(user.password)

    users[user.email] = {
        "name": user.name,
        "password_hash": stored_hashed_password
    }

    return {
        "message": "Registration successful!"
    }


@app.post("/login")
def login(user: UserLogin):

    user_data = users.get(user.email)

    if user_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found!"
        )

    stored_hashed_password = user_data["password_hash"]

    has_matched = password_hash.verify(
        user.password,
        stored_hashed_password
    )

    if not has_matched:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email or password may be wrong!"
        )

    access_token = create_access_token(user.email)

    return {
        "message": "Login successful",
        "access_token": access_token
    }

