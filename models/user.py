
from pydantic import BaseModel





class DSP(BaseModel):
    username: str
    password: str
    nego_api : str
    interactive_nogo_api: str
    request_api : str
    interactive_request_api:str



class DSPShow(BaseModel):
    username:str
    nego_api: str
    request_api: str
    create_date: str