from sqlalchemy.orm import Session
import models
import schemas

def get_post(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()

def get_list_of_posts(db: Session):
    return db.query(models.Post).all()

def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(content=post.content)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def update_post(db: Session, post_id: int, post: schemas.PostUpdate):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    db_post.content = post.content
    db.commit()
    db.refresh(db_post)
    return db_post

def delete_post(db: Session, post_id: int):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    db.delete(db_post)
    db.commit()
    return {"message": "Post deleted successfully"}