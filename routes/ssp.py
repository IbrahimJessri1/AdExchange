from fastapi import APIRouter, HTTPException, status
from repositries.validation import Validator
from models.ssp import  Ad_Request
from repositries import ssp as repo_ssp
ssp_router = APIRouter(
    prefix="/ssp",
    tags = ['SSP']
)


@ssp_router.post('/request')
async def request_ad(ad_request : Ad_Request):
    val_res = Validator.validate_ad_request(ad_request)
    if val_res:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= val_res)
    return  repo_ssp.request_ad(ad_request)


@ssp_router.post('/request_interactive')
async def request_ad(ad_request : Ad_Request):
    val_res = Validator.validate_ad_request(ad_request)
    if val_res:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= val_res)
    return  repo_ssp.request_ad(ad_request, 1)


@ssp_router.get('/request')
async def request_ad():
    return repo_ssp.autoserve_request()

