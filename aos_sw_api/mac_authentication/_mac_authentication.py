from typing import Union

import httpx

from aos_sw_api.validate import validate_200
from ._model import MacAuthenticationModel, MacAuthenticationPortList


class MacAuthentication:

    def __new__(cls, session: Union[httpx.Client, httpx.AsyncClient], **kwargs):
        if isinstance(session, httpx.Client):
            return MacAuthenticationSync(session=session)
        elif isinstance(session, httpx.AsyncClient):
            return MacAuthenticationAsync(session=session)


class MacAuthenticationBase:
    def __init__(self, session: Union[httpx.Client, httpx.AsyncClient]):
        self._session = session
        self._mac_authentication_base_url = "mac-authentication"


class MacAuthenticationSync(MacAuthenticationBase):
    def __init__(self, session: httpx.Client):
        super().__init__(session=session)

    def get_mac_authentication(self) -> MacAuthenticationModel:
        r = self._session.get(url=self._mac_authentication_base_url)
        validate_200(r)
        return MacAuthenticationModel(**r.json())

    def get_mac_authentication_ports(self) -> MacAuthenticationPortList:
        r = self._session.get(url=f"{self._mac_authentication_base_url}/port")
        validate_200(r)
        return MacAuthenticationPortList(**r.json())


class MacAuthenticationAsync(MacAuthenticationBase):
    def __init__(self, session: httpx.AsyncClient):
        super().__init__(session=session)

    async def get_mac_authentication(self) -> MacAuthenticationModel:
        r = await self._session.get(url=self._mac_authentication_base_url)
        validate_200(r)
        return MacAuthenticationModel(**r.json())

    async def get_mac_authentication_ports(self) -> MacAuthenticationPortList:
        r = await self._session.get(url=f"{self._mac_authentication_base_url}/port")
        validate_200(r)
        return MacAuthenticationPortList(**r.json())
