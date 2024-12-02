from fastapi import APIRouter
from sqlalchemy.future import select

from model import Freelance

freelance_router = APIRouter()


@freelance_router.get('/freelances', summary='Get list freelancers', tags=['Freelancers'])
async def get_freelance():
    query = select(Freelance)
    freelance = await Freelance.run_query(query)

    return freelance
