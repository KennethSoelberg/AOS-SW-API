from typing import Union

import httpx

from aos_sw_api.validate import validate_200
from ._model import SpanningTreeModel, SpanningTreePortList


class SpanningTree:

    def __new__(cls, session: Union[httpx.Client, httpx.AsyncClient], **kwargs):
        if isinstance(session, httpx.Client):
            return SpanningTreeSync(session=session)
        elif isinstance(session, httpx.AsyncClient):
            return SpanningTreeAsync(session=session)


class SpanningTreeBase:
    def __init__(self, session: Union[httpx.Client, httpx.AsyncClient]):
        self._session = session
        self._stp_base_url = "stp"


class SpanningTreeSync(SpanningTreeBase):
    def __init__(self, session: httpx.Client):
        super().__init__(session=session)

    def get_stp(self) -> SpanningTreeModel:
        r = self._session.get(url=self._stp_base_url)
        validate_200(r)
        return SpanningTreeModel(**r.json())

    def get_stp_ports(self) -> SpanningTreePortList:
        r = self._session.get(url=f"{self._stp_base_url}/ports")
        validate_200(r)
        return SpanningTreePortList(**r.json())


class SpanningTreeAsync(SpanningTreeBase):
    def __init__(self, session: httpx.AsyncClient):
        super().__init__(session=session)

    async def get_stp(self) -> SpanningTreeModel:
        r = await self._session.get(url=self._stp_base_url)
        validate_200(r)
        return SpanningTreeModel(**r.json())

    async def get_stp_ports(self) -> SpanningTreePortList:
        r = await self._session.get(url=f"{self._stp_base_url}/ports")
        validate_200(r)
        return SpanningTreePortList(**r.json())
