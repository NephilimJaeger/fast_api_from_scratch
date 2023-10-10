from fastapi import FastAPI
from router import blog_get, blog_post
from database import models
from database.db import engine

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/hello")
def root():
    return {"message": "Welcome to my API"}

models.Base.metadata.create_all(engine)



