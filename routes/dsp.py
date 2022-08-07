from fastapi import APIRouter, status
from models.dsp import DSP
from repositries import dsp as repo_dsp

dsp_router = APIRouter(
    prefix="/dsp",
    tags = ['DSP']
)




@dsp_router.post('/', status_code=status.HTTP_201_CREATED)
async def add_dsp(dsp: DSP):
    return repo_dsp.add_dsp()