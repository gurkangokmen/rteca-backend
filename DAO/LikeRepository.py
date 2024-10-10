from sqlalchemy import select, insert, update, delete
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import text
from Entity.Likes import Likes
from Database.Connection import database

class LikeRepository:

    def get_all_likes(self):
        query = select(Likes)
        return query

    def get_like_number_post_by_id(self, post_id: UUID):
        query = select(Likes).where(Likes.post_id == post_id)
        return query

    async def create_like(self, id:UUID ,user_id: UUID, post_id: UUID):
        query = insert(Likes).values(id=id,user_id=user_id, post_id=post_id)
        return query

    
    def remove_like_2(self, post_id: UUID):
        query = delete(Likes).where(Likes.post_id == post_id)
        return query
    
    def remove_like(self, post_id: UUID, user_id: UUID):
        query = delete(Likes).where(Likes.post_id == post_id).where(Likes.user_id == user_id)
        return query

    def check_user_likes_post(self, post_id: UUID, user_id: UUID):
        query = select(Likes).where(Likes.post_id == post_id, Likes.user_id == user_id)
        return query