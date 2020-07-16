import pytest


def test_get_snmpv3(client):
    print(client.snmpv3.get_snmpv3())


def test_get_snmpv3_users(client):
    print(client.snmpv3.get_snmpv3_users())


@pytest.mark.asyncio
async def test_get_snmpv3_async(async_client):
    await async_client.snmpv3.get_snmpv3()


@pytest.mark.asyncio
async def test_get_snmpv3_users_async(async_client):
    await async_client.snmpv3.get_snmpv3_users()
