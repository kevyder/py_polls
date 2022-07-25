from pydantic import BaseModel


class PollBase(BaseModel):
    title: str
    type: str
    is_add_choices_active: bool
    is_voting_active: bool


class Poll(PollBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    name: str


class User(UserBase):
    id: int
    polls: list[Poll] = []

    class Config:
        orm_mode = True
