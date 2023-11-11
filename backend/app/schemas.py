import datetime
import typing
import uuid

import pydantic


class Timestamp(pydantic.BaseModel):
    timestamp: datetime.datetime = pydantic.Field()


class WorkTimeBase(pydantic.BaseModel):
    timestamp_start: typing.Optional[datetime.datetime] = pydantic.Field(None)
    timestamp_stop: typing.Optional[datetime.datetime] = pydantic.Field(None)


class WorkTimeIdentification(pydantic.BaseModel):
    id: uuid.UUID


class WorkTime(WorkTimeBase, WorkTimeIdentification):
    pass


class WorkTimeComplete(WorkTime):
    created_at: datetime.datetime = pydantic.Field()
    modified_at: datetime.datetime = pydantic.Field()


class AbsenceBase(pydantic.BaseModel):
    start_date: datetime.datetime = pydantic.Field()
    stop_date: typing.Optional[datetime.datetime] = pydantic.Field(None)
    type: str = pydantic.Field()


class AbsenceIdentification(pydantic.BaseModel):
    id: uuid.UUID


class Absence(AbsenceBase, AbsenceIdentification):
    pass


class AbsenceComplete(pydantic.BaseModel):
    created_at: datetime.datetime = pydantic.Field()
    modified_at: datetime.datetime = pydantic.Field()
