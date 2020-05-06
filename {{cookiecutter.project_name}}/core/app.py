from pathlib import Path
from typing import List, Any, Mapping

import toml
from aiohttp import web
from aiologger.handlers.files import AsyncFileHandler
from aiologger.logger import Logger

from .handlers import health_check


CONFIG_PATH = Path(__file__).parent.joinpath("config.toml")
LOGS_PATH = Path(__file__).parent.parent.joinpath('logs')


def make_logger(config: Mapping[str, Any]) -> Logger:
    """ Create Logger instance for using async logging """
    handler = AsyncFileHandler(
        filename=str(LOGS_PATH.joinpath(f'{config["filename"]}.log')),
        encoding='utf-8'
    )
    logger = Logger(
        name=config['name'],
        level=config['level'],
    )
    logger.add_handler(handler)
    return logger


def make_routes() -> List[web.RouteDef]:
    """ Setup route table w/ handlers module """
    return [
        web.get("/health", health_check)
    ]


def load_config() -> Mapping[str, Any]:
    """ Make config for using in app internals """
    return toml.loads(open(CONFIG_PATH).read())


async def application() -> web.Application:
    """ Explicit app for setting things up w/ ASGI runner """
    config = load_config()
    app_ = web.Application(client_max_size=config['app']['client_max_size'])
    routes = make_routes()
    app_['logger'] = make_logger(config['logging'])
    app_.add_routes(routes)
    return app_


if __name__ == '__main__':
    web.run_app(application(), port=8090)
