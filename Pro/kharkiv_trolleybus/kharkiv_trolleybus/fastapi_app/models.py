from sqlalchemy import Table, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from fastapi_app.base import Base
from fastapi_app.database import metadata
from datetime import datetime


users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
)

news = Table(
    "news",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("content", String, nullable=False),
    Column("author", String, nullable=False),
    Column("user_id", Integer, ForeignKey("users.id")),
)