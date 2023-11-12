import typing
import uuid

import fastapi
import sqlalchemy.ext.asyncio
import uvicorn

import backend.database.queries
import backend.app.schemas


async def get_db():
    """

    :return:
    """
    db_config = backend.database.queries.get_database_config()
    db = backend.database.queries.create_connection(db_config=db_config)
    try:
        yield db
    finally:
        await db.close()


Connection = typing.Annotated[sqlalchemy.ext.asyncio.AsyncConnection, fastapi.Depends(get_db)]

app = fastapi.FastAPI()


# work
@app.get('/worktime/v1/work/{work_id}')
async def get_single_work(request: fastapi.Request,
                          work_id: uuid.UUID,
                          db: Connection) -> backend.app.schemas.WorkTime:
    """

    :param request:
    :param work_id:
    :param db:
    :return:
    """
    data = await backend.database.queries.get_entry(db=db, entry_id=work_id)
    # TODO: check if data is of type 'work'
    return data


@app.post('/worktime/v1/work/start')
async def start_work(request: fastapi.Request,
                     db: Connection,
                     body: backend.app.schemas.Timestamp):
    """

    :param request:
    :param db:
    :param body:
    :return:
    """
    entry_id = uuid.uuid4()
    entry = dict()
    entry['id'] = entry_id
    entry['start_time'] = body.timestamp
    entry['type'] = 'work'
    await backend.database.queries.create_entry(db=db, entry=entry)
    return {'entry_id': entry_id}


@app.post('/worktime/v1/work/{work_id}/stop')
async def stop_work(request: fastapi.Request,
                    db: Connection,
                    work_id: uuid.UUID,
                    body: backend.app.schemas.Timestamp):
    """

    :param request:
    :param db:
    :param work_id:
    :param body:
    :return:
    """
    updates_for_entry = dict()
    updates_for_entry['stop_time'] = body.timestamp
    await backend.database.queries.modify_entry(db=db, entry_id=work_id, updates_for_entry=updates_for_entry)
    return {'entry_id': work_id}


if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8083)
