from fastapi import FastAPI # type: ignore
from .routers import form
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(form.router)
