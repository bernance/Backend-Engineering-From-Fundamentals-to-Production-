from fastapi import Depends, status, HTTPException,Response, APIRouter
import schemas, models
from database import *
from typing import List

router = APIRouter(
    prefix= "/notes",
    tags = ["Notes"]
)


#Created a note
@router.post("/", response_model=schemas.NoteResponse)
def create_note(note: schemas.CreateNote, db: Session = Depends(get_db)):
    new_note = models.KnowledgeVault(**note.dict())
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note


#Get all notes
@router.get("/", response_model=List[schemas.NoteResponse])
def get_all_notes(db: Session = Depends(get_db)):
    notes = db.query(models.KnowledgeVault).all()
    return notes


#Get a single note

@router.get("/{id}", response_model=schemas.NoteResponse)
def get_single_note(id: int, db: Session = Depends(get_db)):
    note = db.query(models.KnowledgeVault).filter(models.KnowledgeVault.id == id).first()

    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Note with id {id} not found")
    return note

#Delete note
@router.delete("/{id}")
def delete_note(id: int, db: Session = Depends(get_db)):
    notes = db.query(models.KnowledgeVault).filter(models.KnowledgeVault.id == id)

    if notes.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Note with id {id} not found")
    notes.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#Updating a note
@router.put("/{id}", response_model=schemas.NoteResponse)
def update_note(id: int, note: schemas.UpdateNote, db: Session = Depends(get_db)):
    updated_note = db.query(models.KnowledgeVault).filter(models.KnowledgeVault.id == id)
    if updated_note.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Note with id {id} not found")
    updated_note.update(note.dict(), synchronize_session=False)
    db.commit()
    return updated_note.first()
