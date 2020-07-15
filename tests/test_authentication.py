import pytest


def test_get_authentication(client):
    print(client.authentication.get_authentication())


def test_get_authentication_console(client):
    print(client.authentication.get_authentication_console())


def test_get_authentication_ssh(client):
    print(client.authentication.get_authentication_ssh())


@pytest.mark.asyncio
async def test_get_authentication_async(async_client):
    await async_client.authentication.get_authentication()


@pytest.mark.asyncio
async def test_get_authentication_console_async(async_client):
    await async_client.authentication.get_authentication_console()


@pytest.mark.asyncio
async def test_get_authentication_ssh_async(async_client):
    await async_client.authentication.get_authentication_ssh()
