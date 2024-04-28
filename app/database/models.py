from sqlmodel import SQLModel, Field

class SensorBase(SQLModel):
  blockID: int

class SensorDB(SensorBase, table=True):
  id: int = Field(default=None, primary_key=True)
  state: str = 'normal'

class SensorCreate(SensorBase):
  pass

class ResultBase(SQLModel):
  C: float
  sensorID: int

class ResultDB(ResultBase, table=True):
  id: int = Field(default=None, primary_key=True)
  #time: str

class ResultCreate(ResultBase):
  pass

class ChangeBase(SQLModel):
  sensorID: int
  state: str

class ChangeDB(ChangeBase, table=True):
  id: int = Field(default=None, primary_key=True)

class ChangeCreate(ChangeBase):
  pass