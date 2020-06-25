import aiohttp_cors
from engine.api import routes


def setup_routes(app):
    app.router.add_routes(routes)
    cors = aiohttp_cors.setup(
        app,
        defaults={
            '*': aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                allow_headers=('Content-Type', 'Authorization'),
                allow_methods=('GET', 'PUT', 'POST', 'DELETE', 'PATCH'),
            )
        },
    )

    for route in list(app.router.routes()):
        cors.add(route)
