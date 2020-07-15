import pytest


def test_get_sntp(client):
    print(client.sntp.get_sntp())


@pytest.mark.asyncio
async def test_get_sntp_async(async_client):
    await async_client.sntp.get_sntp()
