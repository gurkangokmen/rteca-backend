from sqlalchemy import Column, Integer, String, Table, MetaData, ForeignKey, text, DateTime
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(UUID, primary_key=True)
    content = Column(String)
    post_id = Column(UUID, nullable=False)
    date = Column(String)
    user_id = Column(UUID, nullable=False)