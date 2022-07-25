from pydantic import BaseModel

from .user import User


class Poll(BaseModel):
    title: str
    type: str
    is_add_choices_active: bool
    is_voting_active: bool
    created_by: User
