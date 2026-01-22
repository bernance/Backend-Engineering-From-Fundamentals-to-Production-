#This contains our SQLALCHEMY models(Tables)
from sqlalchemy import Column, Integer, String, Boolean,TIMESTAMP, text
from database import Base




class KnowledgeVault(Base):
    __tablename__ = "notes"


    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    category = Column(String, nullable=False)
    is_archived = Column(Boolean, nullable=False, default=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))
    #updated_at = Column(TIMESTAMP(timezone=True),nullable=True, server_default=text('now()'))





#Creating the user table
class Users(Base):

    __tablename__ = "users"


    id = Column(Integer, primary_key= True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password= Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

