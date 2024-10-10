# coding: utf-8
from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String, text
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import relationship

from db.base_class import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    active = Column(Boolean, nullable=False, default=True)

