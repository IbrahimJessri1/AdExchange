
from models.ssp import Ad_Request
from config.db import dsp_collection
from repositries import generics as gen
import requests
from repositries.utilites import get_dict
from fastapi import status

from pydantic import BaseModel
class Test(BaseModel):
    att: str



async def request_ad(request: Ad_Request):
    
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
            dsp = all_dsp[j]
            data["min_cpc"] = current_cpc
            res = requests.post(url=dsp["nego_api"], json=data)
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
        return {"success" : False, "msg": "try again later"}

    winner_dsp = all_dsp[winner_dsp_info[0]]
    ad_id = winner_dsp_info[1]
    data = {
        "cpc": current_cpc,
        "ad_id":ad_id
    }
    response = requests.post(url= winner_dsp["request_api"], json=data)
    return response.json()