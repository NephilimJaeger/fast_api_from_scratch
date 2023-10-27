from fastapi import FastAPI, Request
from router import blog_get
from router import blog_post
from router import user
from router import article
from database import models
from database.db import engine
from exceptions import StoryException
from fastapi.responses import JSONResponse


app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)



@app.get("/hello")
def root():
    return {"message": "Welcome to my API"}

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exec: StoryException):
    return JSONResponse(status_code=418,
                        content = {'detail':exec.name})

models.Base.metadata.create_all(engine)



