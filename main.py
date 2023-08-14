from fastapi import FastAPI
from database import Base, engine

# Create table in database
Base.metadata.create_all(bind=engine)


app=FastAPI()

from api.comments_api import comments
from api.hashtag_api import hashtags
from api.photo_api import *
from api.posts_api import posts
from api.users_api import users


@app.get('/hello')
async def hello():
    return {'hello': 'Fastapi'}

app.post('/hello')
async def post_home(name: str):
    return {'message': f'Hello {name}'}

