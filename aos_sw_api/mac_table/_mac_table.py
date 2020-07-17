from typing import Union

import httpx

from aos_sw_api.validate import validate_200
from ._model import MacTableEntryList, MacTableEntry


class MacTable:

    def __new__(cls, session: Union[httpx.Client, httpx.AsyncClient], **kwargs):
        if isinstance(session, httpx.Client):
            return MacTableSync(session=session)
        elif isinstance(session, httpx.AsyncClient):
            return MacTableAsync(session=session)


class MacTableBase:
    def __init__(self, session: Union[httpx.Client, httpx.AsyncClient]):
        self._session = session
        self._mac_table_base_url = "mac-table"


class MacTableSync(MacTableBase):
    def __init__(self, session: httpx.Client):
        super().__init__(session=session)

    def get_mac_table(self) -> MacTableEntryList:
        r = self._session.get(url=self._mac_table_base_url)
        validate_200(r)
        return MacTableEntryList(**r.json())

    def get_mac_table_mac_address(self, mac_address: str) -> MacTableEntry:
        r = self._session.get(url=f"{self._mac_table_base_url}/{mac_address}")
        validate_200(r)
        return MacTableEntry(**r.json())

    def get_mac_table_port(self, port_id: str) -> MacTableEntryList:
        r = self._session.get(url=f"ports/{port_id}/{self._mac_table_base_url}")
        validate_200(r)
        return MacTableEntryList(**r.json())

    def get_mac_table_vlan(self, vlan_id: str) -> MacTableEntryList:
        r = self._session.get(url=f"vlans/{vlan_id}/{self._mac_table_base_url}")
        validate_200(r)
        return MacTableEntryList(**r.json())


class MacTableAsync(MacTableBase):
    def __init__(self, session: httpx.AsyncClient):
        super().__init__(session=session)

    async def get_mac_table(self) -> MacTableEntryList:
        r = await self._session.get(url=self._mac_table_base_url)
        validate_200(r)
        return MacTableEntryList(**r.json())

    async def get_mac_table_mac_address(self, mac_address: str) -> MacTableEntry:
        r = await self._session.get(url=f"{self._mac_table_base_url}/{mac_address}")
        validate_200(r)
        return MacTableEntry(**r.json())

    async def get_mac_table_port(self, port_id: str) -> MacTableEntryList:
        r = await self._session.get(url=f"ports/{port_id}/{self._mac_table_base_url}")
        validate_200(r)
        return MacTableEntryList(**r.json())

    async def get_mac_table_vlan(self, vlan_id: str) -> MacTableEntryList:
        r = await self._session.get(url=f"vlans/{vlan_id}/{self._mac_table_base_url}")
        validate_200(r)
        return MacTableEntryList(**r.json())
