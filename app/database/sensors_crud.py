from fastapi import HTTPException
from .models import SensorBase, SensorDB, SensorCreate, ChangeBase, ChangeDB, ChangeCreate
from sqlmodel import Session, select

def create_sensor(session: Session, sensor_in: SensorCreate):
  sensor_db = SensorDB.model_validate(sensor_in)
  session.add(sensor_db)
  session.commit()
  session.refresh(sensor_db)
  return sensor_db

def get_sensors(session: Session, state: str = ''):
  if state != '':
    return session.exec(select(SensorDB).where(SensorDB.state == state)).all()
  return session.exec(select(SensorDB)).all()

def get_sensors_block(session: Session, blockID: int):
  return session.exec(select(SensorDB).where(SensorDB.blockID == blockID)).all()

def get_sensor(session: Session, id: int):
  sensor = session.get(SensorDB, id)
  if not sensor:
    raise HTTPException(status_code=404, detail='ID not found')
  return sensor

def change_state(session: Session, id: int, state: str):
  sensor = session.get(SensorDB, id)
  if not sensor:
    raise HTTPException(status_code=404, detail='ID not found')
  sensor.state = state
  change_log = ChangeDB(sensorID=id, state=state)
  session.add(change_log)
  session.commit()
  session.refresh(sensor)
  return sensor

def change_block(session: Session, id: int, blockID: int):
  sensor = session.get(SensorDB, id)
  if not sensor:
    raise HTTPException(status_code=404, detail='ID not found')
  sensor.blockID = blockID
  session.commit()
  session.refresh(sensor)
  return sensor