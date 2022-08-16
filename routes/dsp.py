from fastapi import APIRouter, status, HTTPException, Depends
from models.user import DSP, DSPUpdate
from repositries import dsp as repo_dsp
from repositries.validation import Validator
from repositries.authorize import Authorize
from models. token import TokenData
from repositries import oauth2

dsp_router = APIRouter(
    prefix="/dsp",
    tags = ['DSP']
)




@dsp_router.post('/', status_code=status.HTTP_201_CREATED)
async def add_dsp(dsp: DSP):
    val_res = Validator.validate_dsp(dsp)
    if val_res:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= val_res)
    return repo_dsp.add_dsp(dsp)


@dsp_router.put('/account')
async def update_account(dsp_update : DSPUpdate, current_username : TokenData = Depends(oauth2.get_current_user)):
    Authorize.auth("self_update_account_dsp", current_username.username)
    val_res = Validator.validate_dsp_update(dsp_update)
    if val_res:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= val_res)
    return repo_dsp.update_dsp_account(dsp_update, current_username.username)


@dsp_router.get('/')
async def my_account(current_username : TokenData = Depends(oauth2.get_current_user)):
    Authorize.auth("self_get_dsp", current_username.username)
    return repo_dsp.get(current_username.username)




@dsp_router.get('/all')
async def get_all_dsp():
    return repo_dsp.get_all_dsp()