from fastapi import APIRouter, status, Depends
from sqlmodel import Session
from ..database.models import SensorBase, SensorDB, SensorCreate
from ..database import sensors_crud
from ..database.database import get_session

router = APIRouter(prefix='/sensors')

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_sensor(*, session: Session = Depends(get_session), sensor_in: SensorCreate):
  sensor = sensors_crud.create_sensor(session, sensor_in)
  return sensor

@router.get('/', response_model=list[SensorDB])
def get_sensors(*, session: Session = Depends(get_session), state: str = ''):
  sensors = sensors_crud.get_sensors(session, state)
  return sensors

@router.get('/{blockID}', response_model=list[SensorDB])
def get_sensors_block(*, session: Session = Depends(get_session), blockID: int):
  sensors = sensors_crud.get_sensors_block(session, blockID)
  return sensors

@router.get('/{id}', response_model=SensorDB)
def get_sensor(*, session: Session = Depends(get_session), id: int):
  return sensors_crud.get_sensor(session, id)

@router.put('/{id}/state')
def change_state(*, session: Session = Depends(get_session), id: int, state: str):
  return sensors_crud.change_state(session, id, state)

@router.put('/{id}/block')
def change_block(*, session: Session = Depends(get_session), id: int, blockID: int):
  return sensors_crud.change_block(session, id, blockID)