from typing import Union

import httpx

from aos_sw_api.validate import validate_200
from ._model import AuthenticationModel, AuthenticationConsole, AuthenticationSsh


class Authentication:

    def __new__(cls, session: Union[httpx.Client, httpx.AsyncClient], **kwargs):
        if isinstance(session, httpx.Client):
            return AuthenticationSync(session=session)
        elif isinstance(session, httpx.AsyncClient):
            return AuthenticationAsync(session=session)


class AuthenticationBase:
    def __init__(self, session: Union[httpx.Client, httpx.AsyncClient]):
        self._session = session
        self._authentication_base_url = "authentication"


class AuthenticationSync(AuthenticationBase):
    def __init__(self, session: httpx.Client):
        super().__init__(session=session)

    def get_authentication(self) -> AuthenticationModel:
        r = self._session.get(url=self._authentication_base_url)
        validate_200(r)
        return AuthenticationModel(**r.json())

    def get_authentication_console(self) -> AuthenticationConsole:
        r = self._session.get(url=f"{self._authentication_base_url}/console")
        validate_200(r)
        return AuthenticationConsole(**r.json())

    def get_authentication_ssh(self) -> AuthenticationSsh:
        r = self._session.get(url=f"{self._authentication_base_url}/ssh")
        validate_200(r)
        return AuthenticationSsh(**r.json())


class AuthenticationAsync(AuthenticationBase):
    def __init__(self, session: httpx.AsyncClient):
        super().__init__(session=session)

    async def get_authentication(self) -> AuthenticationModel:
        r = await self._session.get(url=self._authentication_base_url)
        validate_200(r)
        return AuthenticationModel(**r.json())

    async def get_authentication_console(self) -> AuthenticationConsole:
        r = await self._session.get(url=f"{self._authentication_base_url}/console")
        validate_200(r)
        return AuthenticationConsole(**r.json())

    async def get_authentication_ssh(self) -> AuthenticationSsh:
        r = await self._session.get(url=f"{self._authentication_base_url}/ssh")
        validate_200(r)
        return AuthenticationSsh(**r.json())
