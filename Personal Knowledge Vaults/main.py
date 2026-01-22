from fastapi import FastAPI, Depends, status, HTTPException,Response
import schemas, models, utils
from database import *
from typing import List
from routers import notes, users, auth

app = FastAPI()
models.Base.metadata.create_all(bind=engine)







app.include_router(notes.router)
app.include_router(users.router)
app.include_router(auth.router)

