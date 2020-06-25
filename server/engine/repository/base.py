from typing import Iterable
from aiohttp import web
from peewee import Model


class BaseRepository:
    model = Model

    def __init__(self, app: web.Application):
        self.app = app

    async def get(self, record_id: str) -> self.model:
        # pylint: disable=maybe-no-member
        return await self.app['db'].get(self.model, self.model.id == record_id)

    async def add(self, data: dict) -> self.model:
        return await self.app['db'].create(self.model, **data)

    async def update(self, record_id: str, data: dict):
        # pylint: disable=maybe-no-member
        return await self.app['db'].execute(
            self.model.update(**data).where(self.model.id == record_id)
        )

    async def fetch_all(self, **kwargs) -> Iterable[self.model]:
        return await self.app['db'].execute(self.model.select())
