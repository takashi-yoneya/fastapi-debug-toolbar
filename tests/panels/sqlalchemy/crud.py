import typing as t

from sqlalchemy import Column
from sqlalchemy.orm import Session

from . import models


def create_user(db: Session, username: str) -> models.User:
    user = models.User(username=username)
    db.add(user)
    db.commit()
    return user


def get_user(db: Session, user_id: Column[int]) -> t.Optional[models.User]:
    query = db.query(models.User).filter(models.User.id == user_id)

    if query is not None:
        return query.first()
    return query
