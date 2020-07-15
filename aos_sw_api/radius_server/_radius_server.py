from typing import Union

import httpx

from aos_sw_api.validate import validate_200
from ._model import RadiusServerList, RadiusServerModel


class RadiusServer:

    def __new__(cls, session: Union[httpx.Client, httpx.AsyncClient], **kwargs):
        if isinstance(session, httpx.Client):
            return RadiusServerSync(session=session)
        elif isinstance(session, httpx.AsyncClient):
            return RadiusServerAsync(session=session)


class RadiusServerBase:
    def __init__(self, session: Union[httpx.Client, httpx.AsyncClient]):
        self._session = session
        self._radius_servers_base_url = "radius_servers"


class RadiusServerSync(RadiusServerBase):
    def __init__(self, session: httpx.Client):
        super().__init__(session=session)

    def get_all_radius_servers(self) -> RadiusServerList:
        r = self._session.get(url=self._radius_servers_base_url)
        validate_200(r)
        return RadiusServerList(**r.json())

    def get_one_radius_server(self, radius_server_id: int) -> RadiusServerModel:
        r = self._session.get(url=f"{self._radius_servers_base_url}/{radius_server_id}")
        validate_200(r)
        return RadiusServerModel(**r.json())


class RadiusServerAsync(RadiusServerBase):
    def __init__(self, session: httpx.AsyncClient):
        super().__init__(session=session)

    async def get_all_radius_servers(self) -> RadiusServerList:
        r = await self._session.get(url=self._radius_servers_base_url)
        validate_200(r)
        return RadiusServerList(**r.json())

    async def get_one_radius_server(self, radius_server_id: int) -> RadiusServerModel:
        r = await self._session.get(url=f"{self._radius_servers_base_url}/{radius_server_id}")
        validate_200(r)
        return RadiusServerModel(**r.json())
