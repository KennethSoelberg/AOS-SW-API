from pprint import pprint

import pytest


def test_get_ports_client(client):
    pprint(client.port.get_all_ports().port_element[0].dict())


def test_get_one_port_client(client):
    client.port.get_one_port(port_id="1")


def test_get_all_ports_statistics_client(client):
    client.port.get_all_ports_statistics()


def test_get_one_port_statistics_client(client):
    client.port.get_one_port_statistics(port_id="1")


@pytest.mark.asyncio
async def test_get_ports_async_client(async_client):
    await async_client.port.get_all_ports()


@pytest.mark.asyncio
async def test_get_one_port_async_client(async_client):
    await async_client.port.get_one_port(port_id="1")


@pytest.mark.asyncio
async def test_get_all_ports_statistics_async_client(async_client):
    await async_client.port.get_all_ports_statistics()


@pytest.mark.asyncio
async def test_get_one_port_statistics_async_client(async_client):
    await async_client.port.get_one_port_statistics(port_id="1")
