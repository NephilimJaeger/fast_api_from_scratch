from fastapi import APIRouter, Depends
from database.schemas import UserBase, UserDisplay
from sqlalchemy.orm.session import Session
from database.db import get_db
from database import db_user

router = APIRouter(
    prefix='/user',
    tags=['user']
)

#create user
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase,db: Session = Depends(get_db)):
    return db_user.create_user(db, request)
#read user
#Update user
#Delete user