from pydantic import BaseModel
from enum import Enum
from typing import Optional, List


class Gender(str, Enum):
    MALE= "male"
    FELMALE= "female"




class Language(str, Enum):
    EN= "en"
    AR = "ar"


class UserInfo(BaseModel):
    location: Optional[str] = None
    gender: Optional[Gender] = None
    age: Optional[int] = None
    language: Optional[Language] = None

    
class Category(str, Enum):
    TECHNOLOGY= "technology"

class Categories(BaseModel):
    categories_list: Optional[List[Category]] = None


class AdType(str, Enum):
    TEXT= "text"
    IMAGE= "image"
    VIDEO= "video"

    
class Ad_Request(BaseModel):
    min_cpc: float
    user_info: Optional[UserInfo] = None
    categories: Optional[Categories] = None
    type : AdType