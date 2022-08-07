
from config.db import conn
from . import generics as gen
from fastapi import HTTPException, status
from models.user import DSPShow
from .hashing import Hash
import datetime

def add_dsp(dspInput):
    try:
        collection = conn.AdExchange.user
        dsp = gen.get_one(collection, {"username" : dspInput.username})
        if dsp:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="username is taken!")
        dspInput.password = Hash.bcrypt(dspInput.password)
        dsp = dict(dspInput)
        dsp['role'] = 'dsp'
        dsp["create_date"] = str(datetime.datetime.now())
        collection.insert_one(dsp)
        inserted = gen.get_one(collection, {"username" : dsp['username']})  
        return DSPShow(username=inserted['username'], nego_api= inserted['nego_api'], request_api=inserted['request_api'], create_date=inserted['create_date'])
    except HTTPException as http_excep:
        raise http_excep    
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An Error Happaned, try again later") 