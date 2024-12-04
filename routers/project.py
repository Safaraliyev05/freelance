from fastapi import APIRouter
from sqlalchemy.future import select

from model import Project

project_router = APIRouter()


@project_router.get('/project', summary='Get list projects', tags=['Projects'])
async def get_projects():
    query = select(Project)
    project = await Project.run_query(query)

    return project
