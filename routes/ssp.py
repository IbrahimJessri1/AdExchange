from fastapi import APIRouter, status

from models.ssp import  Ad_Request




ssp_router = APIRouter(
    prefix="/ssp",
    tags = ['SSP']
)




@ssp_router.post('/request')
async def request_ad(ad_request : Ad_Request):
    return 'hi'

