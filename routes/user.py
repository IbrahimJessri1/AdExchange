
from fastapi import APIRouter, status, Depends, HTTPException

from repositries import oauth2, user as repo_user
from models.token import TokenData
from models.user import UserUpdate
from repositries.validation import Validator
from repositries.authorize import Authorize


user_router = APIRouter(
    tags = ['General']
)

@user_router.get('/all')
async def get(current_username : TokenData = Depends(oauth2.get_current_user)):
    Authorize.auth("get_user", current_username.username)
    return repo_user.get_all()


@user_router.put('/update_account')
async def update_account(user_update : UserUpdate, current_username : TokenData = Depends(oauth2.get_current_user)):
    Authorize.auth("self_update_user", current_username.username)
    val_res = Validator.validate_user_update(user_update)
    if val_res:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= val_res)
    return repo_user.update_account(user_update, current_username.username)



@user_router.get('/')
async def get_my_account(current_username : TokenData = Depends(oauth2.get_current_user)):
    Authorize.auth("self_get_user", current_username.username)
    return repo_user.get_my_account(current_username.username)