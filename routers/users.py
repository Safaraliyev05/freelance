from fastapi import APIRouter, HTTPException, status, Query
from sqlalchemy.future import select

from model import User
from schemas.users import CreateUser, ResponseUser, UpdateUser

user_router = APIRouter()


# Users list
@user_router.get('/users', summary='Get list users', tags=['Users'])
async def get_users(
        username: str = Query(None, description="Name of the product to search for"),

):
    query = select(User)
    if username:
        query = query.where(User.username.ilike(f'%{username}%'))

    users = await User.run_query(query)

    return users


# User create
@user_router.post('/user-create', response_model=ResponseUser, summary='Create a user', tags=['Users'])
async def create_user(user: CreateUser) -> ResponseUser:
    return await User.create(**user.model_dump())


# User update
@user_router.patch('/users/{user_id}', summary='Update a user', tags=['Users'])
async def update_user(user_id: int, product: UpdateUser):
    current_user = await User.get(User.id == user_id)
    if current_user:
        await User.update(user_id, **product.model_dump(exclude_unset=True))
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found")
    return f'User updated'


# User delete
@user_router.delete('/users/{user_id}', summary='Delete a user', tags=['Users'])
async def delete_user(user_id: int):
    current_user = await User.get(User.id == user_id)
    if current_user:
        await User.delete(user_id)
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found")
    return "User deleted"
