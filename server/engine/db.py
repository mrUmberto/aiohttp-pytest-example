import peewee_asyncext
from peewee import Model
from engine.config import get_config

config = get_config()

options = {
    'user': config.db_user,
    'password': config.db_password,
    'host': config.db_host,
}

database = peewee_asyncext.PooledPostgresqlExtDatabase(None)


def init_db(db_name: str) -> peewee_asyncext.PooledPostgresqlExtDatabase:
    database.init(db_name, **options)
    return database


class BaseModel(Model):
    class Meta:
        database = database
