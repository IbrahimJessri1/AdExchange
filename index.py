from fastapi import FastAPI

from routes import dsp, authentication,user, ssp

app = FastAPI()


app.include_router(dsp.dsp_router)
app.include_router(authentication.authentication_router)
app.include_router(user.user_router)
app.include_router(ssp.ssp_router)