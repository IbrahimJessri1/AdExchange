
from config.db import dsp_collection
from . import generics as gen
from fastapi import HTTPException, status
from models.user import DSPShow, DSPUpdate
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

def update_dsp_account(dsp_update : DSPUpdate, username):
    try:
        query = { "username": username}
        in_values = {}
        if dsp_update.password:
            in_values["password"] = Hash.bcrypt(dsp_update.password)
        if dsp_update.nego_api:
            in_values["nego_api"] = dsp_update.nego_api
        if dsp_update.interactive_nego_api:
            in_values["interactive_nego_api"] = dsp_update.interactive_nego_api
        if dsp_update.request_api:
            in_values["request_api"] = dsp_update.request_api
        if dsp_update.interactive_request_api:
            in_values["interactive_request_api"] = dsp_update.interactive_request_api
        if dsp_update.html_request_api:
            in_values["html_request_api"] = dsp_update.html_request_api
        if dsp_update.html_interactive_request_api:
            in_values["html_interactive_request_api"] = dsp_update.html_interactive_request_api
        new_values = { "$set": in_values }
        res = gen.update_one(dsp_collection, query, new_values)
        return toDSPShow(res)
    except HTTPException as http_excep:
        raise http_excep    
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An Error Happaned, try again later") 



def get(username):
    try:
        res = gen.get_one(dsp_collection, {"username" : username})
        return toDSPShow(res)
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
        html_request_api=item["html_request_api"],
        html_interactive_request_api=item["html_interactive_request_api"],
        create_date=item["create_date"]
    )

def toDSPShowList(itemList):
    res = []
    for item in itemList:
        res.append(toDSPShow(item))
    return res