from fastapi import APIRouter, status

from models.ssp import  Ad_Request

from repositries import ssp as repo_ssp

from fastapi.responses import JSONResponse 
from pydantic import BaseModel

ssp_router = APIRouter(
    prefix="/ssp",
    tags = ['SSP']
)


class Test(BaseModel):
    msg : str


@ssp_router.post('/request')
async def request_ad(ad_request : Ad_Request):
    return await repo_ssp.request_ad(ad_request)


@ssp_router.post('/request_interactive')
async def request_ad(ad_request : Ad_Request):
    return await repo_ssp.request_ad(ad_request, 1)

