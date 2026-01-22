#This contains the pydantic models
#Schema Validation and all sorts


from pydantic import BaseModel, EmailStr
from datetime import datetime

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


class CreateUser(BaseModel):
    email : EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email : EmailStr
    #password: str
    created_at: datetime

    class config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str