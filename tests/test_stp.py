import pytest


def test_get_stp(client):
    print(client.stp.get_stp())


def test_get_stp_ports(client):
    print(client.stp.get_stp_ports())


@pytest.mark.asyncio
async def test_get_stp_async(async_client):
    await async_client.stp.get_stp()


@pytest.mark.asyncio
async def test_get_stp_ports_async(async_client):
    await async_client.stp.get_stp_ports()
