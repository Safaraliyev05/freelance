from fastapi import APIRouter
from sqlalchemy.future import select

from model import Freelance

freelance_router = APIRouter()


@freelance_router.get('/freelances')
async def get_products():
    query = select(Freelance)
    products = await Freelance.run_query(query)

    return products
