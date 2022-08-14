
from venv import create
from config.db import dsp_collection
from . import generics as gen
from fastapi import HTTPException, status
from models.user import DSPShow
from .hashing import Hash
import datetime

def add_dsp(dspInput):
    try:
        collection = dsp_collection
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


def get_all_dsp():
    dsps = gen.get_many(dsp_collection, {})
    return toDSPShowList(dsps)





def toDSPShow(item):
    return DSPShow(
        username=item["username"],
        nego_api=item["nego_api"],
        interactive_nego_api=item["interactive_nego_api"],
        request_api=item["request_api"],
        interactive_request_api=item["interactive_request_api"],
        create_date=item["create_date"]
    )

def toDSPShowList(itemList):
    res = []
    for item in itemList:
        res.append(toDSPShow(item))
    return res