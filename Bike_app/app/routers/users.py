from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi_sqlalchemy import db

from app.models.schema import User as SchemaUser
from app.models.user import User as UserModel

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/add_user/", tags=["users"], response_model=SchemaUser)
async def add_user(user: SchemaUser):
    user = UserModel(first_name=user.first_name, second_name=user.second_name,
                     phone_number=user.phone_number, password=user.password,
                     email=user.email, description=user.description)
    db.session.add(user)
    db.session.commit()
    return user


@router.get("/users/", tags=["users"])
async def get_users():
    users = db.session.query(UserModel).all()

    return users


@router.get("/users/me", tags=["users"])
async def read_user_me():
    return {"user_id": "the current user"}


@router.get("/users/{user_id}", tags=["users"])
async def read_user(user_id: str):
    return {"user_id": user_id}
