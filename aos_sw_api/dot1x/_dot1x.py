from typing import Union

import httpx

from aos_sw_api.validate import validate_200
from ._model import Dot1xModel, Dot1xAuthenticatorPortList, Dot1xPortSecurityList


class Dot1x:

    def __new__(cls, session: Union[httpx.Client, httpx.AsyncClient], **kwargs):
        if isinstance(session, httpx.Client):
            return Dot1xSync(session=session)
        elif isinstance(session, httpx.AsyncClient):
            return Dot1xAsync(session=session)


class Dot1xBase:
    def __init__(self, session: Union[httpx.Client, httpx.AsyncClient]):
        self._session = session
        self._dot1x_base_url = "dot1x"


class Dot1xSync(Dot1xBase):
    def __init__(self, session: httpx.Client):
        super().__init__(session=session)

    def get_dot1x(self) -> Dot1xModel:
        r = self._session.get(url=self._dot1x_base_url)
        validate_200(r)
        return Dot1xModel(**r.json())

    def get_dot1x_authenticator(self) -> Dot1xAuthenticatorPortList:
        r = self._session.get(url=f"{self._dot1x_base_url}/authenticator")
        validate_200(r)
        return Dot1xAuthenticatorPortList(**r.json())

    def get_dot1x_port_security(self) -> Dot1xPortSecurityList:
        r = self._session.get(url=f"{self._dot1x_base_url}/port_security")
        validate_200(r)
        return Dot1xPortSecurityList(**r.json())


class Dot1xAsync(Dot1xBase):
    def __init__(self, session: httpx.AsyncClient):
        super().__init__(session=session)

    async def get_dot1x(self) -> Dot1xModel:
        r = await self._session.get(url=self._dot1x_base_url)
        validate_200(r)
        return Dot1xModel(**r.json())

    async def get_dot1x_authenticator(self) -> Dot1xAuthenticatorPortList:
        r = await self._session.get(url=f"{self._dot1x_base_url}/authenticator")
        validate_200(r)
        return Dot1xAuthenticatorPortList(**r.json())

    async def get_dot1x_port_security(self) -> Dot1xPortSecurityList:
        r = await self._session.get(url=f"{self._dot1x_base_url}/port_security")
        validate_200(r)
        return Dot1xPortSecurityList(**r.json())
