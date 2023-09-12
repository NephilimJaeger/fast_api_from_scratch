from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional

app = FastAPI()

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to my API"}

# @app.get("/blog/all")
# def get_all_blogs():
#     return {"message":"All blogs provided"}

@app.get("/blog/all")
def get_all_blogs(page=1, page_size: Optional[int] = None):
    return {"message":f"All {page_size} blogs on page {page}"}

@app.get("/blog/{id}/{comment_id}")
def get_commet(id:int,comment_id:int,valid:bool,username: Optional[str] = None):
    return {"message":f"id {id}, comment_id {comment_id},valid {valid}, username {username}"}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@app.get("/blog/type/{type}")
def get_blog_type(type: BlogType):
    return {"message": f"Blog type {type.value}"}

@app.get("/blog/{id}", status_code= status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    return {"message": f"Blog with id {id}"}

