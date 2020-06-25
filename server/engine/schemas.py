from pydantic import BaseModel, validator


class CreateBread(BaseModel):
    class Config:
        orm_mode = True

    name: str


class ResponseBread(CreateBread):
    id: str

    @validator('id', pre=True, always=True)
    def set_id_to_str(cls, v):
        return str(v)
