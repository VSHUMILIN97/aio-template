from aiohttp import web


async def health_check(request: web.Request) -> web.Response:
    """ Application health status handler """
    await request.app['logger'].debug("Health check requested")
    return web.Response(body="App is working", status=200)
