# Knowledge Vault API

A beginner-friendly REST API built with FastAPI while learning backend development fundamentals.

This project focuses on clean structure, proper ORM usage, and request/response validation.

## Tech Stack

- Python
- FastApi
- SQLAlchemy ORM
- PostgreSQL
- Pydantic v2

## Project Structure 

- database.py - Database connection and session management
- models.py - SQLAlchemy ORM models
- schemas.py - Pydantic request and response schemas
- main.py - FastAPI app and routes  


## Features

 - Create, read, update, and delete notes
 - SQLAlchemy ORM for database interaction
 - Pydantic schemas for data validation
 - PostgreSQL as the database backend
 - Clean separation of concerns

## Setup Instructions

- ### Clone the repository
    git clone https://github.com/bernance/Backend-Engineering-From-Fundamentals-to-Production-.git  
    cd Personal Knowledge Vaults
  
- ### Create an activate vitrual environment
    python -m venv venv  
    source venv/bin/activate

- ### Install dependencies
    pip install fastapi uvicorn sqlalchemy psycopg
  
- ### Run the application
    uvicorn main:app --reload


## Learning Goals

This project was built to practice:

 - FastAPI fundamentals
 - SQLAlchemy ORM modeling
 - Database session management
 - Pydantic v2 response validation
 - Backend project structuring



## Future Improvements

- Environment variable configuration

- Pagination

- Authentication

- Database migrations with Alembic

- Improved error handling


## Disclaimer

This is a learning project, built as part of my journey into backend and machine learning engineering. Best practices will be implemented progressively as I advance.

## Author
  Worthy Bernard  
  Backend Developer | Junior ML Engineer


















