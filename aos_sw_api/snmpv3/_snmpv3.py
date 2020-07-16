from typing import Union

import httpx

from aos_sw_api.validate import validate_200
from ._model import SnmpV3Model, SnmpV3UserList


class SnmpV3:

    def __new__(cls, session: Union[httpx.Client, httpx.AsyncClient], **kwargs):
        if isinstance(session, httpx.Client):
            return SnmpV3Sync(session=session)
        elif isinstance(session, httpx.AsyncClient):
            return SnmpV3Async(session=session)


class SnmpV3Base:
    def __init__(self, session: Union[httpx.Client, httpx.AsyncClient]):
        self._session = session
        self._snmpv3_base_url = "snmpv3"


class SnmpV3Sync(SnmpV3Base):
    def __init__(self, session: httpx.Client):
        super().__init__(session=session)

    def get_snmpv3(self) -> SnmpV3Model:
        r = self._session.get(url=self._snmpv3_base_url)
        validate_200(r)
        return SnmpV3Model(**r.json())

    def get_snmpv3_users(self) -> SnmpV3UserList:
        r = self._session.get(url=f"{self._snmpv3_base_url}/users")
        validate_200(r)
        return SnmpV3UserList(**r.json())


class SnmpV3Async(SnmpV3Base):
    def __init__(self, session: httpx.AsyncClient):
        super().__init__(session=session)

    async def get_snmpv3(self) -> SnmpV3Model:
        r = await self._session.get(url=self._snmpv3_base_url)
        validate_200(r)
        return SnmpV3Model(**r.json())

    async def get_snmpv3_users(self) -> SnmpV3UserList:
        r = await self._session.get(url=f"{self._snmpv3_base_url}/users")
        validate_200(r)
        return SnmpV3UserList(**r.json())
