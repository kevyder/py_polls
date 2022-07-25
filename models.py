from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)

    polls = relationship("Poll", back_populates="user")


class Poll(Base):
    __tablename__ = "polls"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    type = Column(String)
    is_add_choices_active = Boolean
    is_voting_active = Boolean

    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="polls")
