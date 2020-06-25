import asyncio
import pytest
import os
import alembic.config
import psycopg2
from faker import Faker


from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from engine.app import init_app
from engine.config import get_config
from engine.config import BasicConfig


def construct_db_uri(config: BasicConfig) -> str:
    return 'postgresql://{user}:{password}@{host}/{db}'.format(
        host=config.db_host, user=config.db_user, password=config.db_password, db=config.db_name
    )


fake = Faker()

config = get_config('test')


con = psycopg2.connect(
    dbname='postgres', user=config.db_user, host=config.db_host, password=config.db_password
)

con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cur = con.cursor()


@pytest.fixture
def faker():
    return fake


@pytest.fixture(scope='session')
def test_db():
    cur.execute('CREATE DATABASE {};'.format(config.db_name))
    yield
    cur.execute('REVOKE CONNECT ON DATABASE {} FROM public;'.format(config.db_name))
    cur.execute(
        """SELECT pg_terminate_backend(pg_stat_activity.pid)"""
        """FROM pg_stat_activity WHERE pg_stat_activity.datname = '{}';""".format(config.db_name)
    )
    cur.execute('DROP DATABASE {}'.format(config.db_name))


@pytest.fixture(scope='function')
def db_and_tables(test_db):
    db_uri = construct_db_uri(config)
    upgrade_args = [
        '-x',
        'custom_db={}'.format(db_uri),
        'upgrade',
        'head',
    ]
    alembic.config.main(argv=upgrade_args)
    yield
    downgrade_args = [
        '-x',
        'custom_db={}'.format(db_uri),
        'downgrade',
        'base',
    ]
    alembic.config.main(argv=downgrade_args)


@pytest.fixture
def app():
    return init_app(config)


@pytest.fixture(scope='session')
def loop():
    return asyncio.get_event_loop()


@pytest.fixture
async def cli(aiohttp_client, app):
    # pylint: disable=redefined-outer-name
    return await aiohttp_client(app)
