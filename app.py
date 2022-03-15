"""
Demo Application
"""
# import random
# from typing import Optional, List

from fastapi import FastAPI
# from fastapi import BackgroundTasks
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel
# from pydantic import EmailStr

import time

"""
class User(BaseModel):
    id: Optional[int] = None
    name: str
    title: Optional[str] = None
    email: EmailStr
    age: Optional[int] = None

class UserNotFoundException(Exception):
    def __init__(self, user_id: int):
        self.user_id = user_id

users: List[User] = [User(id=0, name="initial user", title="Prof.", age=99999999999, email="init@techradar.com")]
current_id = 0

def get_next_user_id():
    global current_id
    current_id += 1
    return current_id

# This is a long running task, the user should not need to wait for this to complete
def add_user_to_database(user):
    time.sleep(random.randint(3,10))
    users.append(user)
    print(f"User {user.id} added to the database")
"""

app = FastAPI()


@app.get("/")
async def root():
    return dict(message="Hello World")

# @app.get("/users/",
#     responses={
#         200: {
#             "description": "Get all users",
#             "content": {
#                 "application/json":{
#                     "example": {
#                         "users": [
#                             {"id": 1, "name": "Tedd Baker", "title": "Mr.", "email": "ted.baker@techradar.com", "age": 45},
#                             {"id": 2, "name": "John Tucker", "title": "Mr.", "email": "survivor@techradar.com", "age": 32},
#                             {"id": 3, "name": "Nolwasi Juta", "title": "Dr.", "email": "njuta@techradar.com", "age": 28},
#                             {"id": 4, "name": "Bob \"Bobbie\" Skinner", "title": "Mr.", "email": "thebobster@techradar.com", "age": 13}
#                         ]
#                     }
#                 }
#             }
#         }
#     }
# )
# async def get_all_users():
#     return {"users": users}

# @app.get("/users/{user_id}",
#     response_model=User, 
#     responses={
#         200: {
#             "description": "The user for the giver user_id",
#             "content": {
#                 "application/json": {
#                     "example": {"id": 12, "name": "Example Name", "title": "Dr.", "email": "example@techradar.com", "age": 45}
#                 }
#             }
#         },
#         404: {
#             "description": "User not found",
#             "content": {
#                 "application/json": {
#                     "message": "User {user_id} could not be found."
#                 }
#             }
#         },
#     }
# )
# async def get_user_by_id(user_id: int):
#     for user in users:
#         if user.id == user_id:
#             return user
#     return JSONResponse(status_code=404, content={"message": "User {} could not be found.".format(user_id)})

# @app.post("/users/",
#     response_model=User, 
#     responses={
#         200: {
#             "description": "The user for the giver user_id",
#             "content": {
#                 "application/json": {
#                     "example": {"id": 12, "name": "Example Name", "title": "Dr.", "email": "example@techradar.com", "age": 45}
#                 }
#             }
#         },
#         400: {
#             "description" : "Unable to create user",
#             "contrent": {
#                 "application/json": {
#                     "example": {"message": "Cannot create a user with a conflicting user_id"}
#                 }
#             }
#         }
#     }
# )
# async def create_user(user: User, background_tasks: BackgroundTasks):
#     if user.id in [user.id for user in users]:
#         return JSONResponse(status_code=400, content={"message": "Cannot create a user with a conflicting user_id"})
#     user.id = get_next_user_id()
#     # add_user_to_database(user)
#     background_tasks.add_task(add_user_to_database, user)
#     return user