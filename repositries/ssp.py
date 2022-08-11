
from http.client import HTTPException
from models.ssp import Ad_Request
from config.db import dsp_collection
from repositries import generics as gen
import requests
from repositries.utilites import get_dict
from fastapi import status

from pydantic import BaseModel
class Test(BaseModel):
    att: str



async def request_ad(request: Ad_Request, interactive = 0):
    
    bid_times = 10

    all_dsp = gen.get_many(dsp_collection, {})
    current_cpc = request.min_cpc
    bid_cpc = request.min_cpc
    winner_dsp_info = [-1, -1]
    data = get_dict(request)
    old_winner = -1
    for _ in range(bid_times):
        for j in range(len(all_dsp)):
            if j == winner_dsp_info[0]:
                continue
            nego_api = "nego_api"
            if interactive != 0:
                nego_api = "interactive_nego_api"
            
            dsp = all_dsp[j]
            data["min_cpc"] = current_cpc
            res = requests.post(url=dsp[nego_api], json=data)
            if res.status_code != status.HTTP_200_OK:
                continue
            res = res.json()
            if res["cpc"] > bid_cpc:
                bid_cpc = res["cpc"]
                winner_dsp_info = [j, res["ad_id"]]
        current_cpc = bid_cpc
        if old_winner == winner_dsp_info[0]:
            break
        old_winner = winner_dsp_info[0]

    if winner_dsp_info[0] == -1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "No Ads For U")

    winner_dsp = all_dsp[winner_dsp_info[0]]
    ad_id = winner_dsp_info[1]
    data = {
        "cpc": current_cpc,
        "ad_id":ad_id
    }
    request_api = "request_api"
    if interactive != 0:
        request_api = "interactive_request_api"
    response = requests.post(url= winner_dsp[request_api], json=data)
    return response.json()