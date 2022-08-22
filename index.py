from fastapi import FastAPI

from routes import dsp, authentication,user, ssp



from fastapi.middleware.cors import CORSMiddleware

from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(dsp.dsp_router)
app.include_router(authentication.authentication_router)
app.include_router(user.user_router)
app.include_router(ssp.ssp_router)



origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)