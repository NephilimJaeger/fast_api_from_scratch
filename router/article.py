from fastapi import APIRouter, Depends
from database.schemas import ArticleBase, ArticleDisplay
from sqlalchemy.orm.session import Session
from database.db import get_db
from database import db_article
from auth.oauth2 import oauth2_scheme

router = APIRouter(
    prefix='/article',
    tags=['article']
)

#Create article
@router.post('/', response_model = ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(db, request)

#Get specific article
@router.get('/{id}', response_model = ArticleDisplay)
def get_specif_article(id: int, db: Session = Depends(get_db), token:str = Depends(oauth2_scheme)):
    return db_article.get_article(db, id)