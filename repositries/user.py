
from config.db import user_collection
from repositries import generics as gen
from .hashing import Hash
from fastapi import HTTPException, status
from models.user import UserShow

def get_all():
    return gen.get_many(user_collection, {})



def update_account(user_update, username):
    try:
        query = { "username": username}
        in_values = {}
        in_values["password"] = Hash.bcrypt(user_update.password)
        new_values = { "$set": in_values }
        res = gen.update_one(user_collection, query, new_values)
        return UserShow(username=res["username"], role=res["role"], create_date=res["create_date"])
    except HTTPException as http_excep:
        raise http_excep    
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An Error Happaned, try again later") 


def get_my_account(username):
    try:
        res = gen.get_one(user_collection, {"username" : username})
        return UserShow(username=res["username"], role=res["role"], create_date=res["create_date"])
    except HTTPException as http_excep:
        raise http_excep    
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An Error Happaned, try again later") 