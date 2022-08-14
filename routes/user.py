
from fastapi import APIRouter, status, Depends

from repositries import oauth2, user as repo_user
from models.token import TokenData
from repositries.authorize import Authorize


user_router = APIRouter(
    tags = ['General']
)

@user_router.get('/all')
async def get(current_username : TokenData = Depends(oauth2.get_current_user)):
    Authorize.auth("get_user", current_username.username)
    return repo_user.get_all()
