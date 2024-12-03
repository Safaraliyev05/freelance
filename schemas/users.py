from pydantic import BaseModel

from model.users import UserStatus


class CreateUser(BaseModel):
    firstname: str | None = None
    lastname: str | None = None
    username: str
    email: str
    phone: str
    status: UserStatus

    class Config:
        from_attributes = True


class ResponseUser(BaseModel):
    id: int
    username: str
    status: int

    class Config:
        from_attributes = True


class UpdateUser(BaseModel):
    firstname: str | None = None
    lastname: str | None = None
    username: str | None = None
    email: str | None = None
    phone: str | None = None
    status: UserStatus | None = None

    class Config:
        from_attributes = True
