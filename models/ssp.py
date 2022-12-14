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
    ANY= "any"
    PLACES= "places"
    Technology= "technology"
    HEALTHCARE = "healthcare"
    APPS= "apps"
    TOYS=  "toys"
    GAMING= "gaming"
    EDUCATION = "education"
    VEHICLES= "vehicles"
    NATURE= "nature"
    FOذOD= "food"
    SMARTPHONES= "smartphones"
    CARS= "cars"
    PRODUCTS= "products"
    WEBSITES= "websites"
    BIKES= "bikes"
    SCHOOL= "school"
    BOOKS= "books"
    ELECTRONICS= "electronics"
    HOUSE= "house"
    FURNITURE= "furniture"
    FAMILY= "family"
    CLOTHES= "clothes"
    WEARBLE= "wearable"
    ANIMALS= "animals"
    MEDIA= "media"
    JOBS= "jobs"



class AdType(str, Enum):
    IMAGE= "image"
    VIDEO= "video"
    GIF= "gif"

class ResponseType(str, Enum):
    JSON= "json"
    HTML= "html"
    
class Shape(str, Enum):
    HORIZONTAL= "horizontal"
    VERTICAL= "vertical"
    RECTANGULAR= "rectangular"


class Ad_Request(BaseModel):
    min_cpc: float
    type : AdType
    user_info: Optional[UserInfo] = {}
    categories: Optional[List[Category]] = []
    keywords: Optional[List[str]] = []
    response_type: ResponseType
    payment_account: str
    max_width: Optional[int] = 0
    max_height: Optional[int] = 0
    shape: Shape