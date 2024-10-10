
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String, text, MetaData
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = MetaData()

class Likes(Base):
    __tablename__ = 'likes'

    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    user_id = Column(UUID, ForeignKey('users.id'), nullable=False)
    post_id = Column(UUID, ForeignKey('posts.id'), nullable=False)
