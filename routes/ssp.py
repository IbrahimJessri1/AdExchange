from fastapi import APIRouter

from models.ssp import  Ad_Request

from repositries import ssp as repo_ssp

ssp_router = APIRouter(
    prefix="/ssp",
    tags = ['SSP']
)


@ssp_router.post('/request')
async def request_ad(ad_request : Ad_Request):
    return await repo_ssp.request_ad(ad_request)


@ssp_router.post('/request_interactive')
async def request_ad(ad_request : Ad_Request):
    return await repo_ssp.request_ad(ad_request, 1)

