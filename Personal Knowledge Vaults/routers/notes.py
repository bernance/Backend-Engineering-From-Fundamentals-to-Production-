from fastapi import Depends, status, HTTPException,Response, APIRouter
import schemas, models, oauth2
from database import *
from typing import List

router = APIRouter(
    prefix= "/notes",
    tags = ["Notes"]
)


#Create a note
@router.post("/", response_model=schemas.NoteResponse)
def create_note(note: schemas.CreateNote, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    new_note = models.KnowledgeVault(owner_id = current_user.id,**note.dict())
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note


#Get all notes
@router.get("/", response_model=List[schemas.NoteResponse])
def get_all_notes(db: Session = Depends(get_db),current_user = Depends(oauth2.get_current_user)):
    notes = db.query(models.KnowledgeVault).filter(models.KnowledgeVault.owner_id == current_user.id).all()
    return notes


#Get a single note

@router.get("/{id}", response_model=schemas.NoteResponse)
def get_single_note(id: int, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    note = db.query(models.KnowledgeVault).filter(models.KnowledgeVault.id == id).first()

    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Note with id {id} not found")
    if note.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Not authorized to carry out this action") 
    return note

#Delete note
@router.delete("/{id}")
def delete_note(id: int, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    notes_query = db.query(models.KnowledgeVault).filter(models.KnowledgeVault.id == id)
    notes = notes_query.first()
    if notes == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Note with id {id} not found")
    if notes.id != current_user.owner_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Not authorized to carry out this action")
    notes_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)






#Updating a note
@router.put("/{id}", response_model=schemas.NoteResponse)
def update_note(id: int, note: schemas.UpdateNote, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    updated_note_query = db.query(models.KnowledgeVault).filter(models.KnowledgeVault.id == id)
    updated_note = updated_note_query.first()
    if updated_note == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Note with id {id} not found")
    if updated_note != current_user.owner_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Not authorized to carry out this action")
    updated_note.update(note.dict(), synchronize_session=False)
    db.commit()
    return updated_note.first()
