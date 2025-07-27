from pydantic import BaseModel, ConfigDict # type: ignore

class FormCreate(BaseModel):
    name: str
    phone: str
    email: str

class FormOut(FormCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
