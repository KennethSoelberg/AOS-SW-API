from typing import Union

import httpx

from aos_sw_api.validate import validate_200
from ._model import PortPoeList, PortPoeStatsList


class Poe:

    def __new__(cls, session: Union[httpx.Client, httpx.AsyncClient], **kwargs):
        if isinstance(session, httpx.Client):
            return PoeSync(session=session)
        elif isinstance(session, httpx.AsyncClient):
            return PoeAsync(session=session)


class PoeBase:
    def __init__(self, session: Union[httpx.Client, httpx.AsyncClient]):
        self._session = session
        self._poe_base_url = "poe"


class PoeSync(PoeBase):
    def __init__(self, session: httpx.Client):
        super().__init__(session=session)

    def get_poe_ports(self) -> PortPoeList:
        r = self._session.get(url=f"{self._poe_base_url}/ports")
        validate_200(r)
        return PortPoeList(**r.json())

    def get_poe_ports_stats(self) -> PortPoeStatsList:
        r = self._session.get(url=f"{self._poe_base_url}/ports/stats")
        validate_200(r)
        return PortPoeStatsList(**r.json())


class PoeAsync(PoeBase):
    def __init__(self, session: httpx.AsyncClient):
        super().__init__(session=session)

    async def get_poe_ports(self) -> PortPoeList:
        r = await self._session.get(url=f"{self._poe_base_url}/ports")
        validate_200(r)
        return PortPoeList(**r.json())

    async def get_poe_ports_stats(self) -> PortPoeStatsList:
        r = await self._session.get(url=f"{self._poe_base_url}/ports/stats")
        validate_200(r)
        return PortPoeStatsList(**r.json())
