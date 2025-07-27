from sqlalchemy import Column, Integer, String # type: ignore
from .database import Base

class FormData(Base):
    __tablename__ = "form_data"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)
