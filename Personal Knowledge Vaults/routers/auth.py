from fastapi import APIRouter, HTTPException, status, Depends, Response
from database import *
import schemas, models, utils, oauth2
from fastapi.security import OAuth2PasswordRequestForm
router = APIRouter()

#Don't forget to import the OauthPassword request form
@router.post("/ulogin")
def user_login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.email == user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= "Invalid credentials")
    if not utils.verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= "Invalid credentials")
    #Here i am using sub and typecasting the user.id to string
    access_token = oauth2.create_access_token(data = {"sub" : str(user.id)})
    return(access_token)