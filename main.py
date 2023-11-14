from fastapi import FastAPI, Request
from router import blog_get
from router import blog_post
from router import user
from router import article
from router import product
from database import models
from database.db import engine
from exceptions import StoryException
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import HTTPException


app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)



@app.get("/hello")
def root():
    return {"message": "Welcome to my API"}

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exec: StoryException):
    return JSONResponse(status_code=418,
                        content = {'detail':exec.name})

# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exec: HTTPException):
#     return PlainTextResponse(str(exec),status_code=400)

models.Base.metadata.create_all(engine)



