from fastapi import FastAPI
from Database.Connection import database
from DAO.PostsRepository import PostsRepository
from Model.PostCreateRequest import PostCreateRequest
from Model.LikeCreateRequest import LikeCreateRequest
from Model.PostUpdateRequest import PostUpdateRequest
from uuid import UUID, uuid4
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()
posts_repository = PostsRepository()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/posts")
async def read_posts():
    query = posts_repository.get_all_posts()
    results = await database.fetch_all(query)
    return results

@app.get("/posts/{post_id}")
async def read_post(post_id: UUID):
    query = posts_repository.get_post_by_id(post_id)
    result = await database.fetch_one(query)
    return result

@app.post("/posts")
async def create_post(request: PostCreateRequest):
    new_id = str(uuid4())

    query = await posts_repository.create_post(id=new_id, user_id=request.user_id, content=request.content, date=request.date)
    await database.execute(query)

    # Fetch the created post
    created_post_query = posts_repository.get_post_by_id(new_id)
    created_post = await database.fetch_one(created_post_query)

    return created_post

@app.put("/posts")
async def update_post(request: PostUpdateRequest):
    query = posts_repository.update_post(post_id=request.post_id, content=request.content, date=request.date)
    await database.execute(query)

    query = posts_repository.get_post_by_id(request.post_id)
    result = await database.fetch_one(query)
    return result

@app.delete("/posts/{post_id}")
async def delete_post(post_id: UUID):
    query = like_repository.remove_like_2(post_id)
    await database.execute(query)

    query = posts_repository.delete_post(post_id)
    await database.execute(query)

    return {"message": "Post deleted successfully"}







# Like Repository
from DAO.LikeRepository import LikeRepository
like_repository = LikeRepository()

@app.get("/likes")
async def likes_list():
    query = like_repository.get_all_likes()
    results = await database.fetch_all(query)
    return results

@app.get("/likes/{post_id}")
async def likes_number(post_id: UUID):
    query = like_repository.get_like_number_post_by_id(post_id)
    result = await database.fetch_all(query)
    return result.__len__()

@app.get("/likes/{post_id}/{user_id}")
async def check_user_likes_post(post_id: UUID, user_id: UUID):
    query = like_repository.check_user_likes_post(post_id,user_id)
    result = await database.fetch_one(query)

    if result is None:
        return False
    else:
        return True

@app.post("/likes")
async def create_like(request: LikeCreateRequest):
    query = like_repository.check_user_likes_post(user_id=request.user_id, post_id=request.post_id)
    result = await database.fetch_one(query)

    if result is None:
        new_id = str(uuid4())

        query = await like_repository.create_like(id=new_id, user_id=request.user_id, post_id=request.post_id)
        await database.execute(query)

        return {"message": "Like created successfully"}
    else:
        return {"message": "User already liked this post"}

    


@app.delete("/likes/{post_id}/{user_id}")
async def remove_like(post_id: UUID, user_id: UUID):
    query = like_repository.remove_like(post_id, user_id)
    await database.execute(query)

    return {"message": "Like removed successfully"}