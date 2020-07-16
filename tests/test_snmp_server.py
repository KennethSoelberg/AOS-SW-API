import pytest


def test_get_snmp_server(client):
    print(client.snmp_server.get_snmp_server())


def test_get_snmp_server_communities(client):
    print(client.snmp_server.get_snmp_server_communities())


def test_get_snmp_server_hosts(client):
    print(client.snmp_server.get_snmp_server_hosts())


def test_get_snmp_server_traps(client):
    print(client.snmp_server.get_snmp_server_traps())


@pytest.mark.asyncio
async def test_get_snmp_server_async(async_client):
    await async_client.snmp_server.get_snmp_server()


@pytest.mark.asyncio
async def test_get_snmp_server_communities_async(async_client):
    await async_client.snmp_server.get_snmp_server_communities()


@pytest.mark.asyncio
async def test_get_snmp_server_hosts_async(async_client):
    await async_client.snmp_server.get_snmp_server_hosts()


@pytest.mark.asyncio
async def test_get_snmp_server_traps_async(async_client):
    await async_client.snmp_server.get_snmp_server_traps()
