import pytest


def test_get_dot1x(client):
    print(client.dot1x.get_dot1x())


def test_get_dot1x_authenticator(client):
    print(client.dot1x.get_dot1x_authenticator())


def test_get_dot1x_port_security(client):
    print(client.dot1x.get_dot1x_port_security())


@pytest.mark.asyncio
async def test_get_dot1x_async(async_client):
    await async_client.dot1x.get_dot1x()


@pytest.mark.asyncio
async def test_get_dot1x_authenticator_async(async_client):
    await async_client.dot1x.get_dot1x_authenticator()


@pytest.mark.asyncio
async def test_get_dot1x_port_security_async(async_client):
    await async_client.dot1x.get_dot1x_port_security()
