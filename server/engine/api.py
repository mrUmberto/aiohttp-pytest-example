import logging
from aiohttp import web
from aiohttp_cors import CorsViewMixin
from engine.schemas import CreateBread, ResponseBread

routes = web.RouteTableDef()

logger = logging.getLogger(__name__)


@routes.view('/api/v1/bread')
class BreadAPIView(web.View, CorsViewMixin):
    async def get(self):
        breads = await self.request.app['repository'].bread.fetch_all()
        return web.json_response([ResponseBread.from_orm(bread).dict() for bread in breads])

    async def post(self):
        request_data = await self.request.json()
        serialized_data = CreateBread(**request_data).dict()
        bread = await self.request.app['repository'].bread.add(serialized_data)
        return web.json_response({'bread_id': ResponseBread.from_orm(bread).json()})
