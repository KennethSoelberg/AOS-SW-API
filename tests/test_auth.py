import pytest


def test_auth_client(client):
    assert client._session.headers["cookie"]


@pytest.mark.asyncio
async def test_auth_async_client(async_client):
    assert async_client._session.headers["cookie"]
