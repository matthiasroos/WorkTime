import os
import typing
import uuid

import dotenv
import sqlalchemy
import sqlalchemy.engine.url
import sqlalchemy.ext.asyncio

import backend.database.models


def get_database_config() -> dict[str, str]:
    """

    :return:
    """
    dotenv.load_dotenv()
    db_config = dict()

    db_config['username'] = os.environ.get('DB_USER')
    db_config['password'] = os.environ.get('DB_PASSWORD')
    db_config['host'] = os.environ.get('DB_HOST')
    db_config['port'] = os.environ.get('DB_PORT')
    db_config['database'] = os.environ.get('DB_SCHEMA')

    db_config['drivername'] = 'postgresql+asyncpg'

    return db_config


def create_connection(db_config: dict[str, str]) -> sqlalchemy.ext.asyncio.AsyncConnection:
    """

    :param db_config:
    :return:
    """
    engine = sqlalchemy.ext.asyncio.create_async_engine(sqlalchemy.engine.url.URL.create(**db_config)).connect()

    return engine


async def create_entry(db: sqlalchemy.ext.asyncio.AsyncConnection, entry: dict):
    """

    :param db:
    :param entry:
    :return:
    """
    async with db as connection:
        await connection.execute(sqlalchemy.insert(backend.database.models.Entry).values(**entry))
        await connection.commit()
    return


async def get_entry(db: sqlalchemy.ext.asyncio.AsyncConnection, entry_id: uuid.UUID) -> typing.Any:
    """

    :param db:
    :param entry_id:
    :return:
    """
    async with db as connection:
        entry_model = backend.database.models.Entry
        result = await connection.execute(
            sqlalchemy.select(
                entry_model,
            ).where(entry_model.id == entry_id))
    return result.first()


async def modify_entry(db: sqlalchemy.ext.asyncio.AsyncConnection, entry_id: uuid.UUID, updates_for_entry: dict):
    """

    :param db:
    :param entry_id:
    :param updates_for_entry:
    :return:
    """
    async with db as connection:
        entry_model = backend.database.models.Entry
        await connection.execute(
            sqlalchemy.update(entry_model).where(entry_model.id == entry_id).values(**updates_for_entry))
        await connection.commit()
    return
