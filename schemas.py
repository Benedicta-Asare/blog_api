from pydantic import BaseModel
from typing import Optional 
from datetime import datetime

class PostBase(BaseModel):
    #author: str
    content: str
    
class PostCreate(PostBase):
    pass

class PostRead(PostBase):
    id: int
    created_at: datetime 
    updated_at: Optional[datetime]

class PostUpdate(PostBase):
    id: int
    updated_at: datetime

class Post(PostBase):
    id: int
    created_at: datetime

    class Config:  # This is to make the response model work
        orm_mode = True