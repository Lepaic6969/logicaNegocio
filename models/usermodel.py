from pydantic import BaseModel

class UserIn(BaseModel):
    email: str
    password: str


class UserOut(BaseModel):
    name: str
    last_name: str
    department: str
    clearance : int
    document_1 : str
    estado_1:str
    caducidad_1:str
    document_2 : str
    estado_2:str
    caducidad_2:str
