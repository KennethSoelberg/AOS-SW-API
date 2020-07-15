from typing import Union

import httpx

from aos_sw_api.validate import validate_200
from ._model import VlanPortList


class VlanPort:

    def __new__(cls, session: Union[httpx.Client, httpx.AsyncClient], **kwargs):
        if isinstance(session, httpx.Client):
            return VlanPortSync(session=session)
        elif isinstance(session, httpx.AsyncClient):
            return VlanPortAsync(session=session)


class VlanPortBase:
    def __init__(self, session: Union[httpx.Client, httpx.AsyncClient]):
        self._session = session
        self._vlan_port_base_url = "vlans-ports"


class VlanPortSync(VlanPortBase):
    def __init__(self, session: httpx.Client):
        super().__init__(session=session)

    def get_all_vlan_ports(self) -> VlanPortList:
        r = self._session.get(url=self._vlan_port_base_url)
        validate_200(r)
        return VlanPortList(**r.json())


class VlanPortAsync(VlanPortBase):
    def __init__(self, session: httpx.AsyncClient):
        super().__init__(session=session)

    async def get_all_vlan_ports(self) -> VlanPortList:
        r = await self._session.get(url=self._vlan_port_base_url)
        validate_200(r)
        return VlanPortList(**r.json())
