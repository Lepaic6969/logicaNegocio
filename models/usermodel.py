from pydantic import BaseModel

class UserIn(BaseModel):
    email: str
    password: str


class UserOut(BaseModel):
    name: str
    last_name: str
    department: str
    clearance : int
    documents : dict