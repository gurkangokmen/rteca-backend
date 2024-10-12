from sqlalchemy import Column, Integer, String, Table, MetaData, ForeignKey, text, DateTime
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = MetaData()

class Posts(Base):
    __tablename__ = 'posts'
    #id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    id = Column(UUID, primary_key=True)
    content = Column(String)
    user_id = Column(UUID, nullable=False)
    date = Column(String)


    

    
# Alternatively, if you are using Table
# posts_table = Table(
#     'posts', metadata,
#     Column('id', Integer, primary_key=True, index=True),
#     Column('content', String)
# )