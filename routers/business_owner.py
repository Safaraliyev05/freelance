from fastapi import APIRouter
from sqlalchemy.future import select

from model import BusinessOwner

b_owner = APIRouter()


@b_owner.get('/business_owners')
async def get_products():
    query = select(BusinessOwner)
    products = await BusinessOwner.run_query(query)

    return products
