import pytest

from aos_sw_api import IpAddress
from aos_sw_api.enums import IpAddressVersionEnum, TimeServerProtocolEnum


def test_get_system_client(client):
    client.system.get_system()


def test_update_system_client(client):
    test_location = "hej"
    old_system = client.system.get_system()
    client.system.update_system(location=test_location)
    new_system = client.system.get_system()
    assert new_system.location == test_location
    client.system.update_system(name=old_system.name, location=old_system.location, contact=old_system.contact)


def test_get_system_status_client(client):
    client.system.get_system_status()


def test_get_system_time_client(client):
    print(client.system.get_system_time())


def test_update_system_time_client(client):
    old_system_time = client.system.get_system_time()
    time_server_ip_1 = IpAddress(version=IpAddressVersionEnum.IAV_IP_V4, octets="10.46.46.46")
    client.system.update_system_time(time_server_protocol=TimeServerProtocolEnum.TSP_SNTP,
                                     time_servers=[time_server_ip_1],
                                     use_sntp_unicast=True)
    new_system = client.system.get_system_time()
    assert new_system.time_servers[0].ip_address.octets == "10.46.46.46"
    client.system.update_system_time(time_server_protocol=old_system_time.time_server_protocol,
                                     time_servers=[IpAddress(**time_server.ip_address.dict()) for time_server in
                                                   old_system_time.time_servers],
                                     use_sntp_unicast=old_system_time.use_sntp_unicast)


@pytest.mark.asyncio
async def test_get_system_async_client(async_client):
    await async_client.system.get_system()


@pytest.mark.asyncio
async def test_update_system_async_client(async_client):
    test_location = "hej"
    old_system = await async_client.system.get_system()
    await async_client.system.update_system(location=test_location)
    new_system = await async_client.system.get_system()
    assert new_system.location == test_location
    await async_client.system.update_system(name=old_system.name, location=old_system.location,
                                            contact=old_system.contact)


@pytest.mark.asyncio
async def test_get_system_status_async_client(async_client):
    await async_client.system.get_system_status()


@pytest.mark.asyncio
async def test_get_system_time_async_client(async_client):
    await async_client.system.get_system_time()


@pytest.mark.asyncio
async def test_update_system_time_async_client(async_client):
    old_system_time = await async_client.system.get_system_time()
    time_server_ip_1 = IpAddress(version=IpAddressVersionEnum.IAV_IP_V4, octets="10.46.46.46")
    await async_client.system.update_system_time(time_server_protocol=TimeServerProtocolEnum.TSP_SNTP,
                                                 time_servers=[time_server_ip_1],
                                                 use_sntp_unicast=True)
    new_system = await async_client.system.get_system_time()
    assert new_system.time_servers[0].ip_address.octets == "10.46.46.46"
    await async_client.system.update_system_time(time_server_protocol=old_system_time.time_server_protocol,
                                                 time_servers=[IpAddress(**time_server.ip_address.dict()) for
                                                               time_server in
                                                               old_system_time.time_servers],
                                                 use_sntp_unicast=old_system_time.use_sntp_unicast)
