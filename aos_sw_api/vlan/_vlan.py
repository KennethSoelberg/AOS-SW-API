from typing import Union

import httpx

from aos_sw_api.validate import validate_200
from ._model import VlanList


class Vlan:

    def __new__(cls, session: Union[httpx.Client, httpx.AsyncClient], **kwargs):
        if isinstance(session, httpx.Client):
            return VlanSync(session=session)
        elif isinstance(session, httpx.AsyncClient):
            return VlanAsync(session=session)


class VlanBase:
    def __init__(self, session: Union[httpx.Client, httpx.AsyncClient]):
        self._session = session
        self._vlan_base_url = "vlans"


class VlanSync(VlanBase):
    def __init__(self, session: httpx.Client):
        super().__init__(session=session)

    def get_all_vlans(self) -> VlanList:
        r = self._session.get(url=self._vlan_base_url)
        validate_200(r)
        return VlanList(**r.json())


class VlanAsync(VlanBase):
    def __init__(self, session: httpx.AsyncClient):
        super().__init__(session=session)

    async def get_all_vlans(self) -> VlanList:
        r = await self._session.get(url=self._vlan_base_url)
        validate_200(r)
        return VlanList(**r.json())
