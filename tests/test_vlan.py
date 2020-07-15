import pytest


def test_get_all_vlan(client):
    print(client.vlan.get_all_vlans())


@pytest.mark.asyncio
async def test_get_all_vlan_async(async_client):
    await async_client.vlan.get_all_vlans()
