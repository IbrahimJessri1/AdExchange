
from sqlite3 import OperationalError
from typing import Optional
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
    html_request_api: str
    html_interactive_request_api: str


class DSPShow(BaseModel):
    username:str
    nego_api : str
    interactive_nego_api: str
    request_api : str
    interactive_request_api:str
    html_request_api: str
    html_interactive_request_api:str
    create_date:str

class DSPUpdate(BaseModel):
    password: Optional[str] = None
    nego_api : Optional[str] = None
    interactive_nego_api: Optional[str] = None
    request_api : Optional[str] = None
    interactive_request_api:Optional[str] = None
    html_request_api: Optional[str] = None
    html_interactive_request_api: Optional[str] = None


class UserUpdate(BaseModel):
    password:str


class UserShow(BaseModel):
    username: str
    role : Role
    create_date:str