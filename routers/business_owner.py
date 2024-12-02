from fastapi import APIRouter
from sqlalchemy.future import select

from model import BusinessOwner

b_owner = APIRouter()


@b_owner.get('/business_owners', summary='List of business owners', tags=['Business owners'])
async def get_owners():
    query = select(BusinessOwner)
    owner = await BusinessOwner.run_query(query)

    return owner
