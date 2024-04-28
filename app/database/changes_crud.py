from fastapi import HTTPException
from .models import ChangeBase, ChangeDB, ChangeCreate
from sqlmodel import Session, select

def get_changes(session: Session):
  return session.exec(select(ChangeDB)).all()