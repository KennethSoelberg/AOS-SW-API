import pytest


def test_get_all_ip_address(client):
    print(client.ip_address_subnet.get_all_ip_address())


@pytest.mark.asyncio
async def test_get_all_ip_address_async(async_client):
    await async_client.ip_address_subnet.get_all_ip_address()
