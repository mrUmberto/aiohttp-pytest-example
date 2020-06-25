import importlib
import inspect
import logging
import os
import pkgutil

from engine.repository.base import BaseRepository

logger = logging.getLogger(__name__)

REPOSITORIES_PKG = ('engine.repository',)


def setup(app):
    async def on_startup(_app):
        _app['repository'] = await Model.create(_app)

    async def on_cleanup(_app):
        await _app['repository'].close()

    app.on_startup.append(on_startup)
    app.on_cleanup.append(on_cleanup)


class Model:
    def __init__(self, app):
        pkgdirs = (
            os.path.dirname(importlib.import_module(pkg).__file__) for pkg in REPOSITORIES_PKG
        )
        for idx, pkgdir in enumerate(pkgdirs):
            for (_, name, _) in pkgutil.iter_modules([pkgdir]):
                module_name = '{}.{}'.format(REPOSITORIES_PKG[idx], name)
                module = importlib.import_module(module_name)

                def is_class_member(member):
                    return (
                        inspect.isclass(member)
                        and member.__module__ == module.__name__
                        and issubclass(member, BaseRepository)
                    )

                for _, cls in inspect.getmembers(module, is_class_member):
                    self.__dict__.update({name: cls(app)})

                logger.debug('Load module "{}"'.format(module_name))

    @staticmethod
    async def create(app):
        self = Model(app)
        return self

    async def close(self):
        pass
