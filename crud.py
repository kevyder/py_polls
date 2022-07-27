import schemas
from database import Session
from models import Poll, User


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: schemas.User):
    db_user = User(email=user.email, name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_polls(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Poll).offset(skip).limit(limit).all()


def create_poll(db: Session, poll: schemas.Poll):
    db_poll = Poll(
        title=poll.title,
        type=poll.type,
        is_add_choices_active=poll.is_add_choices_active,
        is_voting_active=poll.is_voting_active,
        user_id=poll.user_id,
    )
    db.add(db_poll)
    db.commit()
    db.refresh(db_poll)
    return db_poll
