from fastapi import APIRouter
from sqlalchemy.future import select

from model import User
from schemas.users import CreateUser, ResponseUser

user_router = APIRouter()


@user_router.get('/users', summary='Get list users', tags=['Users'])
async def get_users():
    query = select(User)
    users = await User.run_query(query)

    return users


@user_router.post('/user-create', response_model=ResponseUser, summary='Create a user', tags=['Users'])
async def create_user(user: CreateUser) -> ResponseUser:
    new_user = await User.create(**user.model_dump())
    return ResponseUser.from_orm(new_user)
