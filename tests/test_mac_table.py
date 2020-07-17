import pytest


def test_get_mac_table(client):
    print(client.mac_table.get_mac_table())


def test_get_mac_table_mac_address(client):
    print(client.mac_table.get_mac_table_mac_address(mac_address="00085d-79eaa9"))


def test_get_mac_table_port(client):
    print(client.mac_table.get_mac_table_port(port_id="3"))


def test_get_mac_table_vlan(client):
    print(client.mac_table.get_mac_table_vlan(vlan_id=636))


@pytest.mark.asyncio
async def test_get_mac_table_async(async_client):
    await async_client.mac_table.get_mac_table()


@pytest.mark.asyncio
async def test_get_mac_table_mac_address_async(async_client):
    await async_client.mac_table.get_mac_table_mac_address(mac_address="00085d-79eaa9")


@pytest.mark.asyncio
async def test_get_mac_table_port_async(async_client):
    await async_client.mac_table.get_mac_table_port(port_id="3")


@pytest.mark.asyncio
async def test_get_mac_table_vlan_async(async_client):
    await async_client.mac_table.get_mac_table_vlan(vlan_id=636)
