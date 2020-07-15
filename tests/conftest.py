import asyncio

import pytest

from aos_sw_api import Client, AsyncClient


@pytest.fixture(scope="session")
def settings():
    from .user_pass_ip import username, password, switch_ip, api_version
    return dict(username=username, password=password, switch_ip=switch_ip, api_version=api_version)


@pytest.fixture(scope="session")
def client(settings):
    with Client(**settings) as client:
        yield client


@pytest.fixture(scope='session')
def event_loop():
    return asyncio.new_event_loop()


@pytest.fixture(scope="session")
async def async_client(settings):
    async with AsyncClient(**settings) as client:
        yield client
