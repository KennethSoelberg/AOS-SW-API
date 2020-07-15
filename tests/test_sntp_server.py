import pytest


def test_get_sntp(client):
    print(client.sntp_server_details.get_all_sntp_servers())


@pytest.mark.asyncio
async def test_get_sntp_async(async_client):
    await async_client.sntp_server_details.get_all_sntp_servers()
