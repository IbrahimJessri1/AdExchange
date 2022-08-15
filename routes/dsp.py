from fastapi import APIRouter, status, HTTPException
from models.user import DSP
from repositries import dsp as repo_dsp
from repositries.validation import Validator

dsp_router = APIRouter(
    prefix="/dsp",
    tags = ['DSP']
)




@dsp_router.post('/', status_code=status.HTTP_201_CREATED)
async def add_dsp(dsp: DSP):
    val_res = Validator.validate_dsp(dsp)
    if val_res:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= val_res)
    return 'hi'
    return repo_dsp.add_dsp(dsp)



@dsp_router.get('/')
async def get_all_dsp():
    return repo_dsp.get_all_dsp()