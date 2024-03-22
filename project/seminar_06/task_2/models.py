from pydantic import BaseModel, Field, EmailStr
from datetime import date


class UserIn(BaseModel):
    firstname: str = Field(..., min_length=2, title='Задается имя пользователя')
    lastname: str = Field(..., min_length=2, title='Задается фамилия пользователя')
    birthday: date = Field(..., title='Задается день рождения пользователя в формате "YYYY-MM-DD"')
    email: EmailStr = Field(..., title='Задается email пользователя')
    address: str = Field(default=None, min_length=5, title='Задается адрес пользователя')


class User(UserIn):
    id: int = Field(title="ID")