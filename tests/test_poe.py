import pytest


def test_get_poe_ports(client):
    print(client.poe.get_poe_ports())


def test_get_poe_ports_stats(client):
    print(client.poe.get_poe_ports_stats())


@pytest.mark.asyncio
async def test_get_poe_ports_async(async_client):
    await async_client.poe.get_poe_ports()


@pytest.mark.asyncio
async def test_get_poe_ports_stats_async(async_client):
    await async_client.poe.get_poe_ports_stats()
