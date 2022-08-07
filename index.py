from fastapi import FastAPI

from routes import dsp

app = FastAPI()


app.include_router(dsp.dsp_router)