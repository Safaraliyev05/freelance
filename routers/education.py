from fastapi import APIRouter
from sqlalchemy.future import select

from model import Education

education = APIRouter()


@education.get('/education', summary='List of Educations', tags=['Education'])
async def get_education():
    query = select(Education)
    education = await Education.run_query(query)

    return education
