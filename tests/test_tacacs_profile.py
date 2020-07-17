import pytest


def test_get_tacacs_profile(client):
    print(client.tacacs_profile.get_tacacs_profile())


@pytest.mark.asyncio
async def test_get_tacacs_profile_async(async_client):
    await async_client.tacacs_profile.get_tacacs_profile()
