from pydantic import BaseModel


class User(BaseModel):
    first_name: str
    second_name: str
    phone_number: str
    password: str
    email: str
    description: str

    class Config:
        orm_mode = True

