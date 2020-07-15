import pytest


def test_get_all_radius_servers(client):
    client.radius_server.get_all_radius_servers()


def test_get_one_radius_server(client):
    client.radius_server.get_one_radius_server(radius_server_id=1)


@pytest.mark.asyncio
async def test_get_all_radius_servers_async(async_client):
    await async_client.radius_server.get_all_radius_servers()


@pytest.mark.asyncio
async def test_get_one_radius_server_async(async_client):
    await async_client.radius_server.get_one_radius_server(radius_server_id=1)
