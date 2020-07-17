import pytest


def test_get_syslog(client):
    print(client.syslog.get_syslog())


@pytest.mark.asyncio
async def test_get_syslog_async(async_client):
    await async_client.syslog.get_syslog()
