from pydantic import BaseModel

class MemoryCreate(BaseModel):
    text: str


class MemoryOut(BaseModel):
    id: int
    text: str

    class Config:
        from_attributes = True