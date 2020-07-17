import pytest


def test_get_transceivers(client):
    print(client.transceivers.get_transceivers())


@pytest.mark.asyncio
async def test_get_transceivers_async(async_client):
    await async_client.transceivers.get_transceivers()
