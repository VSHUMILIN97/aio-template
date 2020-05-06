from typing import List, Dict

import attr
import pytest

from core.app import application


@attr.s
class Logger:

    logs: Dict[str, List[str]] = attr.ib()

    async def debug(self, msg):
        self.logs['debug'].append(msg)

    async def info(self, msg):
        self.logs['info'].append(msg)

    async def warning(self, msg):
        self.logs['warning'].append(msg)

    async def error(self, msg):
        self.logs['error'].append(msg)

    async def critical(self, msg):
        self.logs['critical'].append(msg)

    warn = warning
    fatal = critical


@pytest.fixture()
def logs():
    """ Current app logs storage """
    saved_logs = {
        'debug': [], 'info': [], 'warning': [], 'error': [], 'critical': []
    }
    yield saved_logs
    for storage in saved_logs.values():
        storage.clear()


@pytest.fixture
def web_client(loop, aiohttp_client, logs):
    """ Fixture for emulating external client """
    app_ = loop.run_until_complete(application())
    app_['logger'] = Logger(logs)  # Do not use real logger in tests
    return loop.run_until_complete(aiohttp_client(app_))
