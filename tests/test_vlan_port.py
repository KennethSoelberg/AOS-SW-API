import pytest


def test_get_all_vlan_ports(client):
    print(client.vlan_port.get_all_vlan_ports())


@pytest.mark.asyncio
async def test_get_all_vlan_ports_async(async_client):
    await async_client.vlan_port.get_all_vlan_ports()
