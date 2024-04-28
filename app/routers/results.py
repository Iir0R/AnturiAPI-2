from fastapi import APIRouter, status, Depends
from sqlmodel import Session
from ..database.models import ResultBase, ResultDB, ResultCreate
from ..database import results_crud
from ..database.database import get_session

router = APIRouter(prefix='/results')

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_result(*, session: Session = Depends(get_session), result_in: ResultCreate):
  result = results_crud.create_result(session, result_in)
  return result

@router.delete('/{id}')
def delete_result(*, session: Session = Depends(get_session), id: int):
  return results_crud.delete_result(session, id)