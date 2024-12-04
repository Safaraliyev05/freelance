from fastapi import APIRouter, HTTPException, status
from sqlalchemy.future import select

from model import Freelance
from schemas.freelance import CreateFreelance, UpdateFreelance

freelance_router = APIRouter()


@freelance_router.get('/freelances', summary='Get list freelancers', tags=['Freelancers'])
async def get_freelance():
    query = select(Freelance)
    freelance = await Freelance.run_query(query)

    return freelance


@freelance_router.post('/freelance-create', summary='Create a freelance', tags=['Freelancers'])
async def create_freelance(freelance: CreateFreelance):
    return await Freelance.create(**freelance.model_dump())


# Freelance update
@freelance_router.patch('/freelances/{freelance_id}', summary='Update a freelance', tags=['Freelancers'])
async def update_freelance(freelance_id: int, freelance: UpdateFreelance):
    current_freelance = await Freelance.get(Freelance.id == freelance_id)
    if current_freelance:
        await Freelance.update(freelance_id, **freelance.model_dump(exclude_unset=True))
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Freelancer not found")
    return f'Freelancer updated'


# Freelance delete
@freelance_router.delete('/freelances/{freelance_id}', summary='Delete a freelance', tags=['Freelancers'])
async def delete_freelance(freelance_id: int):
    current_freelance = await Freelance.get(Freelance.id == freelance_id)
    if current_freelance:
        await Freelance.delete(freelance_id)
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Freelancer not found")
    return "Freelancer deleted"
