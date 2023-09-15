from fastapi import APIRouter, status, Response
from enum import Enum
from typing import Optional

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

@router.get("/all",
         summary = "Retrieve all blogs",
         description= "This api call simulates fetching all blogs",
         response_description= "The list of all available blogs")
def get_all_blogs(page=1, page_size: Optional[int] = None):
    return {"message":f"All {page_size} blogs on page {page}"}

@router.get("/{id}/{comment_id}",
         tags = ['comment'])
def get_commet(id:int,comment_id:int,valid:bool,username: Optional[str] = None):
    """
    Simulates retrieving a comment of a blog
    - **id** mandatory path parameter
    - **comment_id** mandatory path parameter
    - **valid** optional query parameter
    - **username** optional query parameter

    """
    return {"message":f"id {id}, comment_id {comment_id},valid {valid}, username {username}"}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@router.get("/type/{type}")
def get_blog_type(type: BlogType):
    return {"message": f"Blog type {type.value}"}

@router.get("/{id}",
         status_code= status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    return {"message": f"Blog with id {id}"}