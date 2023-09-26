from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):
    content: str
    
class PostCreate(PostBase):
    pass

class PostRead(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime

class PostUpdate(PostBase):
    id: int
    updated_at: datetime

class Post(PostBase):
    id: int

