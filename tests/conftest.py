import pytest


@pytest.fixture()
def settings():
    from .user_pass_ip import username, password, switch_ip, api_version
    return dict(username=username, password=password, switch_ip=switch_ip, api_version=api_version)
