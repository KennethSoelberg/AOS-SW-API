import pytest


def test_get_mac_authentication(client):
    print(client.mac_authentication.get_mac_authentication())


def test_get_mac_authentication_ports(client):
    print(client.mac_authentication.get_mac_authentication_ports())


@pytest.mark.asyncio
async def test_get_mac_authentication_async(async_client):
    await async_client.mac_authentication.get_mac_authentication()


@pytest.mark.asyncio
async def test_get_mac_authentication_ports_async(async_client):
    await async_client.mac_authentication.get_mac_authentication_ports()
