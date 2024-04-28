from fastapi import HTTPException
from .models import ResultBase, ResultDB, ResultCreate, SensorDB
from sqlmodel import Session, select

def create_result(session: Session, result_in: ResultCreate):
  result_db = ResultDB.model_validate(result_in)
  session.add(result_db)
  session.commit()
  session.refresh(result_db)
  return result_db

def delete_result(session: Session, id: int):
  result = session.get(ResultDB, id)
  if not result:
    raise HTTPException(status_code=404, detail='ID not found')
  session.delete(result)
  session.commit()
  return {'message': f'Result wit ID {id} deleted'}