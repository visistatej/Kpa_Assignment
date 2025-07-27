from fastapi import APIRouter, Depends # type: ignore
from sqlalchemy.orm import Session # type: ignore
from .. import crud, schemas, database

router = APIRouter(prefix="/form", tags=["Form"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/submit", response_model=schemas.FormOut)
def submit_form(form: schemas.FormCreate, db: Session = Depends(get_db)):
    return crud.create_form(db, form)

@router.get("/details", response_model=list[schemas.FormOut])
def get_all_forms(db: Session = Depends(get_db)):
    return crud.get_forms(db)
