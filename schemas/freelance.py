from pydantic import BaseModel


class CreateFreelance(BaseModel):
    education: list | None = None
    project: list | None = None
    skills: str

    class Config:
        from_attributes = True


class UpdateFreelance(BaseModel):
    education: list | None = None
    project: list | None = None
    skills: list | None = None

    class Config:
        from_attributes = True
