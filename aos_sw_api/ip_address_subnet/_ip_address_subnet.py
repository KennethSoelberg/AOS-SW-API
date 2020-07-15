from typing import Union

import httpx

from aos_sw_api.validate import validate_200
from ._model import IpAddressSubnetList


class IpAddressSubnet:

    def __new__(cls, session: Union[httpx.Client, httpx.AsyncClient], **kwargs):
        if isinstance(session, httpx.Client):
            return IpAddressSubnetSync(session=session)
        elif isinstance(session, httpx.AsyncClient):
            return IpAddressSubnetAsync(session=session)


class IpAddressSubnetBase:
    def __init__(self, session: Union[httpx.Client, httpx.AsyncClient]):
        self._session = session
        self._vlan_base_url = "vlans"
        self._ipaddress_base_url = "ipaddresses"


class IpAddressSubnetSync(IpAddressSubnetBase):
    def __init__(self, session: httpx.Client):
        super().__init__(session=session)

    def get_all_ip_address(self) -> IpAddressSubnetList:
        r = self._session.get(url=self._ipaddress_base_url)
        validate_200(r)
        return IpAddressSubnetList(**r.json())


class IpAddressSubnetAsync(IpAddressSubnetBase):
    def __init__(self, session: httpx.AsyncClient):
        super().__init__(session=session)

    async def get_all_ip_address(self) -> IpAddressSubnetList:
        r = await self._session.get(url=self._ipaddress_base_url)
        validate_200(r)
        return IpAddressSubnetList(**r.json())
