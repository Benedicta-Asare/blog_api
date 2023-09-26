from sqlalchemy import Column, Integer, String, TIMESTAMP, text
from database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    content = Column(String)
    created_at = Column(
        TIMESTAMP(timezone=True), 
        server_default=text("now()"), 
        nullable=False
    )
    updated_at = Column(
        TIMESTAMP(timezone=True), 
        server_default=text("now()"), 
        onupdate=text("now()"), 
        nullable=False
    )