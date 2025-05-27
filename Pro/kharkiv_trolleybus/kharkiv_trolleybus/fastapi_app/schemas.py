from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str

class User(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class NewsCreate(BaseModel):
    title: str
    content: str
    author: str
    user_id: int
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class News(BaseModel):
    id: int
    title: str
    content: str
    author: str
    created_at: datetime

    class Config:
        orm_mode = True