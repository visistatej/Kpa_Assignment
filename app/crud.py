from sqlalchemy.orm import Session # type: ignore
from . import models, schemas

def create_form(db: Session, form: schemas.FormCreate):
    db_form = models.FormData(**form.dict())
    db.add(db_form)
    db.commit()
    db.refresh(db_form)
    return db_form

def get_forms(db: Session):
    return db.query(models.FormData).all()
