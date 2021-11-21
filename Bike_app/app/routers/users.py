from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi_sqlalchemy import db


from app.models.schema import User as SchemaUser
from app.models.user import User as UserModel, User


router = APIRouter()
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


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


# @router.get("/users/me", tags=["users"])
# async def read_users_me(current_user: User = Depends(get_current_user2)):
#     return current_user


