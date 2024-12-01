from fastapi import APIRouter
from sqlalchemy.future import select

from model import User

user_router = APIRouter()


@user_router.get('/products')
async def get_products():
    query = select(User)
    products = await User.run_query(query)

    return products
