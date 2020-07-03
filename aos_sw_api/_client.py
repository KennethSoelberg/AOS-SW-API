from typing import Union

import httpx

from aos_sw_api.auth import Auth


class BaseClient:

    def __init__(self,
                 switch_ip: str,
                 api_version: int,
                 sync: bool,
                 username: str,
                 password: str,
                 https: bool,
                 auto_logout: bool,
                 cert_path: Union[str, bool]):

        if https:
            base_url = f"https://{switch_ip}/rest/v{api_version}/"
        else:
            base_url = f"http://{switch_ip}/rest/v{api_version}/"

        self._auto_logout = auto_logout

        client_settings = dict(base_url=base_url, verify=cert_path)
        if sync:
            self._session = httpx.Client(**client_settings)
        else:
            self._session = httpx.AsyncClient(**client_settings)

        # ArubaOS-Switch REST api does not support keep-alive
        # Disable http keep-alive
        self._session.headers["Connection"] = "close"

        self.auth = Auth(session=self._session, username=username, password=password)


class Client(BaseClient):

    def __init__(self,
                 switch_ip: str,
                 api_version: int,
                 username: str,
                 password: str,
                 https: bool = True,
                 auto_logout: bool = True,
                 cert_path: Union[str, bool] = False):
        super().__init__(switch_ip=switch_ip,
                         api_version=api_version,
                         sync=True,
                         username=username,
                         password=password,
                         https=https,
                         auto_logout=auto_logout,
                         cert_path=cert_path)

    def __enter__(self):
        self.auth.login()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._session: httpx.Client
        if self._auto_logout:
            self.auth.logout()
        self._session.close()

    def close_session(self):
        self._session: httpx.Client
        self._session.close()


class AsyncClient(BaseClient):

    def __init__(self,
                 switch_ip: str,
                 api_version: int,
                 username: str,
                 password: str,
                 https: bool = True,
                 auto_logout: bool = True,
                 cert_path: Union[str, bool] = False):
        super().__init__(switch_ip=switch_ip,
                         api_version=api_version,
                         sync=False,
                         username=username,
                         password=password,
                         https=https,
                         auto_logout=auto_logout,
                         cert_path=cert_path)

    async def __aenter__(self):
        await self.auth.login()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._auto_logout:
            await self.auth.logout()
        await self._session.aclose()

    async def close_session(self):
        await self._session.aclose()
