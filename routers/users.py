from fastapi import APIRouter
from sqlalchemy.future import select

from model import User

user_router = APIRouter()


@user_router.get('/users')
async def get_users():
    query = select(User)
    users = await User.run_query(query)

    return users
