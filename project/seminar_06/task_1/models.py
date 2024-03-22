from pydantic import BaseModel, Field, EmailStr


class UserIn(BaseModel):
    username: str = Field(title="Имя пользователя", min_length=3, max_length=50)
    email: EmailStr = Field(title="Адрес эл. почты", max_length=128)
    password: str = Field(title="Пароль", min_length=3, max_length=128)


class User(UserIn):
    id: int = Field(title="ID")
    email: EmailStr = Field(max_length=128)

