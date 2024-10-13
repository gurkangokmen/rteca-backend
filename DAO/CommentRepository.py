from sqlalchemy import select, insert, update, delete
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import text
from datetime import datetime
from Entity.Comments import Comments
from Database.Connection import database

class CommentRepository:

    def get_comments_by_id(self, post_id: UUID):
        query = select(Comments).where(Comments.post_id == post_id)
        return query
    
    async def create_comment(self,id:UUID ,content: str, post_id: UUID, date: datetime, user_id: UUID):
        query = insert(Comments).values(id=id, content=content, post_id=post_id, date=date, user_id=user_id)
        return query
    
    def delete_commnets_by_post_id(self, post_id: UUID):
        query = delete(Comments).where(Comments.post_id == post_id)
        return query
