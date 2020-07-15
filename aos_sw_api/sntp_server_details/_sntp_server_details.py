from typing import Union

import httpx

from aos_sw_api.validate import validate_200
from ._model import SntpServerDetailsList


class SntpServerDetails:

    def __new__(cls, session: Union[httpx.Client, httpx.AsyncClient], **kwargs):
        if isinstance(session, httpx.Client):
            return SntpServerDetailsSync(session=session)
        elif isinstance(session, httpx.AsyncClient):
            return SntpServerDetailsAsync(session=session)


class SntpServerDetailsBase:
    def __init__(self, session: Union[httpx.Client, httpx.AsyncClient]):
        self._session = session
        self._sntp_server_base_url = "system/sntp_server"


class SntpServerDetailsSync(SntpServerDetailsBase):
    def __init__(self, session: httpx.Client):
        super().__init__(session=session)

    def get_all_sntp_servers(self) -> SntpServerDetailsList:
        r = self._session.get(url=self._sntp_server_base_url)
        validate_200(r)
        return SntpServerDetailsList(**r.json())


class SntpServerDetailsAsync(SntpServerDetailsBase):
    def __init__(self, session: httpx.AsyncClient):
        super().__init__(session=session)

    async def get_all_sntp_servers(self) -> SntpServerDetailsList:
        r = await self._session.get(url=self._sntp_server_base_url)
        validate_200(r)
        return SntpServerDetailsList(**r.json())
