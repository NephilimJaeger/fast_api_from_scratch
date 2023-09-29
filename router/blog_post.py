from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import Optional


router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class Image(BaseModel):
    url:str
    alias:str
class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool]
    tags: list[str] = []
    metadata: dict[str, str] = {'key':'val1'}
    image: Optional[Image] = None

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        "id": id,
        "data":blog,
        "version": version}

@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog:BlogModel, id: int, 
                   comment_title: str = Query(None,
                                            title='Title of the comment',
                                            description = 'Some description for comment_id',
                                            alias = 'commentTitle',
                                            deprecated=True),
                                        content:str =  Body(...,   #required parameter
                                                            min_length=10,
                                                            max_length=50,
                                                            regex='^[a-z\s]*$'),
                                        v : Optional[list[str]] = Query(None),
                                        comment_id: int = Path(gt=5, le=10)):
    return {'blog':blog,
            'id':id,
            'comment_title': comment_title,
            'content': content,
            'version': v,
            'comment_id': comment_id}

def required_functionality():
    return {'message': 'Learning FastAPI is important'}