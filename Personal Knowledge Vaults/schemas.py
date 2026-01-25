#This contains the pydantic models
#Schema Validation and all sorts

from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime
#============================#
#Schema validation for the Notes
#============================#
class NoteBase(BaseModel):
    title: str
    content: str
    category: str
    is_archived: bool=False

class CreateNote(NoteBase):
    pass


class NoteResponse(NoteBase):
    pass


class UpdateNote(BaseModel):
    title: str
    content: str
    category: str

#============================#
#Schema validation for User
#============================#
class CreateUser(BaseModel):
    email : EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email : EmailStr
    #password: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }
    #I used the above instead of this below due to pydantic v2 syntax:
    #class Config:
        #orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

#============================#
#Schema validation for the access token
#============================#
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel): 
    sub: str
    #Instead of using id: Optional[str] = None, I used the above because standard jwt uses jwt to store user id
    #and it is always a string and don't make it optional since a standard token always have sub