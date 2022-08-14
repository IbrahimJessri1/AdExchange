
from pydantic import BaseModel

from enum import Enum

class Role(str, Enum):
    ADMIN= "admin"

class User(BaseModel):
    username: str
    password: str
    role: Role


class DSP(BaseModel):
    username: str
    password: str
    nego_api : str
    interactive_nego_api: str
    request_api : str
    interactive_request_api:str



class DSPShow(BaseModel):
    username:str
    nego_api : str
    interactive_nego_api: str
    request_api : str
    interactive_request_api:str
    create_date:str


