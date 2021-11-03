import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Request, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from starlette.responses import JSONResponse


from app.models.user import User as UserModel
from app.routers import users

load_dotenv(".env")

app = FastAPI()

app.include_router(users.router)

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
