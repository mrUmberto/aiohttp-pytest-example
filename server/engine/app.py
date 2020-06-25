import peewee_async

from aiohttp import web
from engine.db import init_db
from engine.config import get_config, BasicConfig
from engine.services import setup as setup_repository
from engine.routes import setup_routes


def init_app(config: BasicConfig = get_config()) -> web.Application:
    current_app = web.Application()
    database = init_db(config.db_name)
    database.set_allow_sync(False)
    current_app['config'] = config
    current_app['db'] = peewee_async.Manager(database)
    setup_repository(current_app)
    setup_routes(current_app)
    return current_app


app = init_app()
