from fastapi import APIRouter, HTTPException, status, Depends, Response
from database import *
import schemas, models, utils
router = APIRouter()

@router.post("/ulogin")
def user_login(user_credentials: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.email == user_credentials.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= "Invalid credentials")
    if not utils.verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= "Invalid credentials")
    
    return("Login sucessful")