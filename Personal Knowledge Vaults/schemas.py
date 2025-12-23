#This contains the pydantic models
#Schema Validation and all sorts


from pydantic import BaseModel

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