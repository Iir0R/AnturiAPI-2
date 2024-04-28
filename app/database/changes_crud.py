from fastapi import HTTPException
from .models import ChangeBase, ChangeDB, ChangeCreate
from sqlmodel import Session, select

def get_changes(session: Session, sensorID: int):
  return session.exec(select(ChangeDB).where(ChangeDB.sensorID == sensorID)).all()