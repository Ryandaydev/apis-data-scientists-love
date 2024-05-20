"""SQLAlchemy Query Functions"""
from sqlalchemy.orm import Session

import models

def get_players(db: Session):
    query = db.query(models.Player)
    return query