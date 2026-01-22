from fastapi import FastAPI, Depends, status, HTTPException,Response, APIRouter
import schemas, utils, models
from database import *
from typing import List


router = APIRouter(
    prefix= "/userss",
    tags= ["Users"])
#Creating the User functionalities

#Creating a user account
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return(new_user)


#Get all users
@router.get("/", response_model=List[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.Users).all()
    return users


#get a single User
@router.get("/{id}", response_model = schemas.UserResponse)
def get_user(id: int, db:Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} does not exist")
    return user

# delete a user
@router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.id == id)
    if user.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} does not exist")
    user.delete(synchronize_session=False)

    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


#Update a note
@router.put("/{id}", response_model=schemas.UserResponse)
def update_user(id: int, updated_user: schemas.CreateUser, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.id == id)
    if user.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The User with id {id} does not exist")
    user.update(updated_user.dict(), synchronize_session=False)

    db.commit()
    return user.first()


