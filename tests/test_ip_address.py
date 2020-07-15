import pytest

from aos_sw_api import IpAddress
from aos_sw_api.enums import IpAddressVersionEnum


def test_create_ip_address():
    IpAddress(version=IpAddressVersionEnum.IAV_IP_V4, octets="127.0.0.1")
    IpAddress(version=IpAddressVersionEnum.IAV_IP_V6, octets="::1")


def test_wrong_version():
    with pytest.raises(ValueError):
        IpAddress(version="test", octets="127.0.0.1")


def test_wrong_version_vs_ip():
    with pytest.raises(ValueError):
        IpAddress(version=IpAddressVersionEnum.IAV_IP_V6, octets="127.0.0.1")
    with pytest.raises(ValueError):
        IpAddress(version=IpAddressVersionEnum.IAV_IP_V4, octets="::1")
