import pytest

import aos_sw_api


def test_auth_client(settings):
    with aos_sw_api.Client(**settings) as client:
        assert client._session.headers["cookie"]

@pytest.mark.asyncio
async def test_auth_async_client(settings):
    async with aos_sw_api.AsyncClient(**settings) as client:
        assert client._session.headers["cookie"]
