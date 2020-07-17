import pytest


def test_send_cmd(client):
    print(client.cmd.send_command(cmd="show vlan 1 | inc Name"))


@pytest.mark.asyncio
async def test_get_sntp_async(async_client):
    await async_client.cmd.send_command(cmd="show vlan 1 | inc Name")
