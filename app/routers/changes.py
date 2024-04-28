from fastapi import APIRouter, status, Depends
from sqlmodel import Session
from ..database.models import ChangeBase, ChangeDB, ChangeCreate
from ..database import changes_crud
from ..database.database import get_session

router = APIRouter(prefix='/changes')

@router.get('/', response_model=list[ChangeDB])
def get_changes(*, session: Session = Depends(get_session)):
  changes = changes_crud.get_changes(session)
  return changes