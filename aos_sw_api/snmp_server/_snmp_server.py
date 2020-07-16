from typing import Union

import httpx

from aos_sw_api.validate import validate_200
from ._model import SnmpServerModel, SnmpServerCommunityList, SnmpServerHostList, SnmpServerTraps


class SnmpServer:

    def __new__(cls, session: Union[httpx.Client, httpx.AsyncClient], **kwargs):
        if isinstance(session, httpx.Client):
            return SnmpServerSync(session=session)
        elif isinstance(session, httpx.AsyncClient):
            return SnmpServerAsync(session=session)


class SnmpServerBase:
    def __init__(self, session: Union[httpx.Client, httpx.AsyncClient]):
        self._session = session
        self._snmp_server_base_url = "snmp-server"


class SnmpServerSync(SnmpServerBase):
    def __init__(self, session: httpx.Client):
        super().__init__(session=session)

    def get_snmp_server(self) -> SnmpServerModel:
        r = self._session.get(url=self._snmp_server_base_url)
        validate_200(r)
        return SnmpServerModel(**r.json())

    def get_snmp_server_communities(self) -> SnmpServerCommunityList:
        r = self._session.get(url=f"{self._snmp_server_base_url}/communities")
        validate_200(r)
        return SnmpServerCommunityList(**r.json())

    def get_snmp_server_hosts(self) -> SnmpServerHostList:
        r = self._session.get(url=f"{self._snmp_server_base_url}/hosts")
        validate_200(r)
        return SnmpServerHostList(**r.json())

    def get_snmp_server_traps(self) -> SnmpServerTraps:
        r = self._session.get(url=f"{self._snmp_server_base_url}/traps")
        validate_200(r)
        return SnmpServerTraps(**r.json())


class SnmpServerAsync(SnmpServerBase):
    def __init__(self, session: httpx.AsyncClient):
        super().__init__(session=session)

    async def get_snmp_server(self) -> SnmpServerModel:
        r = await self._session.get(url=self._snmp_server_base_url)
        validate_200(r)
        return SnmpServerModel(**r.json())

    async def get_snmp_server_communities(self) -> SnmpServerCommunityList:
        r = await self._session.get(url=f"{self._snmp_server_base_url}/communities")
        validate_200(r)
        return SnmpServerCommunityList(**r.json())

    async def get_snmp_server_hosts(self) -> SnmpServerHostList:
        r = await self._session.get(url=f"{self._snmp_server_base_url}/hosts")
        validate_200(r)
        return SnmpServerHostList(**r.json())

    async def get_snmp_server_traps(self) -> SnmpServerTraps:
        r = await self._session.get(url=f"{self._snmp_server_base_url}/traps")
        validate_200(r)
        return SnmpServerTraps(**r.json())
