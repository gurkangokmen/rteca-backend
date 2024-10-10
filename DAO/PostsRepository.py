from sqlalchemy import select, insert, update, delete
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import text
from Entity.Posts import Posts
from Database.Connection import database

class PostsRepository:

    def get_all_posts(self):
        query = select(Posts)
        return query

    def get_post_by_id(self, post_id: UUID):
        query = select(Posts).where(Posts.id == post_id)
        return query

    async def create_post(self,id:UUID ,user_id: UUID, content: str):
        query = insert(Posts).values(id=id,user_id=user_id, content=content)
        return query

    async def update_post(self, post_id: UUID, content: str):
        query = update(Posts).where(Posts.id == post_id).values(content=content)
        return query

    def delete_post(self, post_id: UUID):
        query = delete(Posts).where(Posts.id == post_id)
        return query