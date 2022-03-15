"""
Demo Application
"""
from typing import Optional, List

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import asyncio

import time

class User(BaseModel):
    id: Optional[int] = None
    name: str
    title: Optional[str] = None
    email: str
    age: Optional[int] = None

class UserNotFoundException(Exception):
    def __init__(self, user_id: int):
        self.user_id = user_id

users: List[User] = []

def get_next_user_id():
    ids = []
    if len(users) == 0:
        return 1
    for user in users:
        ids.append(user.id)
        print("sleeping...")
        time.sleep(1)
        print("done")
    ids.sort()
    return ids[-1] + 1


async def get_next_user_id_async():
    ids = []
    if len(users) == 0:
        return 1
    for user in users:
        ids.append(user.id)
        print("sleeping...")
        asyncio.sleep(1)
        print("done")
    ids.sort()
    return ids[-1] + 1



app = FastAPI()


@app.get("/")
async def root():
    return dict(message="Hello World")

@app.get("/users/{user_id}",
    response_model=User, 
    responses={
        200: {
            "description": "The user for the giver user_id",
            "content": {
                "application/json": {
                    "example": {"id": 12, "name": "Example Name", "title": "Dr.", "email": "example@techradar.com", "age": 45}
                }
            }
        },
        404: {
            "description": "User not found",
            "content": {
                "application/json": {
                    "message": "User {user_id} could not be found."
                }
            }
        },
    }
)
async def get_user_by_id(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return JSONResponse(status_code=404, content={"message": "User {} could not be found.".format(user_id)})

@app.post("/users/",
    response_model=User, 
    responses={
        200: {
            "description": "The user for the giver user_id",
            "content": {
                "application/json": {
                    "example": {"id": 12, "name": "Example Name", "title": "Dr.", "email": "example@techradar.com", "age": 45}
                }
            }
        },
        400: {
            "description" : "Unable to create user",
            "contrent": {
                "application/json": {
                    "example": {"message": "Cannot create a user with a conflicting user_id"}
                }
            }
        }
    }
)
def create_user(user: User):
    if user.id in [user.id for user in users]:
        return JSONResponse(status_code=400, content={"message": "Cannot create a user with a conflicting user_id"})
    user.id = get_next_user_id()
    users.append(user)

    return user

@app.post("/users/async",
    response_model=User, 
    responses={
        200: {
            "description": "The user for the giver user_id",
            "content": {
                "application/json": {
                    "example": {"id": 12, "name": "Example Name", "title": "Dr.", "email": "example@techradar.com", "age": 45}
                }
            }
        },
        400: {
            "description" : "Unable to create user",
            "contrent": {
                "application/json": {
                    "example": {"message": "Cannot create a user with a conflicting user_id"}
                }
            }
        }
    }
)
async def create_user_async(user: User):
    if user.id in [user.id for user in users]:
        return JSONResponse(status_code=400, content={"message": "Cannot create a user with a conflicting user_id"})
    user.id = await get_next_user_id_async()
    users.append(user)

    return user