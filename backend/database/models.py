
import sqlalchemy.dialects.postgresql
import sqlalchemy.orm


Base = sqlalchemy.orm.declarative_base()


class Entry(Base):
    """
    Table Entries
    """
    __tablename__ = 'entries'

    id = sqlalchemy.Column(
        sqlalchemy.dialects.postgresql.UUID(as_uuid=True), primary_key=True, index=True, unique=True
    )
    start_time = sqlalchemy.Column(sqlalchemy.DateTime())
    stop_time = sqlalchemy.Column(sqlalchemy.DateTime())
    type = sqlalchemy.Column(sqlalchemy.String(10))
    created_at = sqlalchemy.Column(sqlalchemy.DateTime(),
                                   default=sqlalchemy.func.now())
    modified_at = sqlalchemy.Column(sqlalchemy.DateTime(),
                                    default=sqlalchemy.func.now(),
                                    onupdate=sqlalchemy.func.now())
