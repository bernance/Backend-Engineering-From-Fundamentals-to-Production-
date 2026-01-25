from jose import JWTError, jwt
from datetime import datetime, timedelta
import schemas, models
from database import *
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer('ulogin')


ALGORITHM = "HS256"
SECRET_KEY = "This is a very random secret key that i choose"
ACCESS_TOKEN_EXPIRATION_MINUTES = 30

#Creating an access token
def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRATION_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt

#Verifying the access token
def verify_access_token(token, credential_exception):
    try:
        #Decode the token
        payload = jwt.decode(token, SECRET_KEY, [ALGORITHM])
        #instead of writing this below
        #id = payload.get("user.id")
        #do this
        
        #Get the user id from the token
        user_id = payload.get("sub")
        if user_id is None:
            raise credential_exception
        #Create TokenData object
        #We used sub because of how we used it in the schemas and the we type casted user_id to string because string is the required type
        token_data = schemas.TokenData(sub = str(user_id))
    except JWTError as e:
        print(e)
        raise credential_exception
    return token_data
    
#Getting the current user
def get_current_user(token:str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credential_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    token_data = verify_access_token(token, credential_exception)
    user = db.query(models.Users).filter(models.Users.id == int(token_data.sub)).first()
    if user is None:
        raise credential_exception
    return user

