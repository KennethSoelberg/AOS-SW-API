from typing import Union

import httpx

from aos_sw_api.validate import validate_200
from ._model import SntpModel


class Sntp:

    def __new__(cls, session: Union[httpx.Client, httpx.AsyncClient], **kwargs):
        if isinstance(session, httpx.Client):
            return SntpSync(session=session)
        elif isinstance(session, httpx.AsyncClient):
            return SntpAsync(session=session)


class SntpBase:
    def __init__(self, session: Union[httpx.Client, httpx.AsyncClient]):
        self._session = session
        self._sntp_base_url = "system/sntp"


class SntpSync(SntpBase):
    def __init__(self, session: httpx.Client):
        super().__init__(session=session)

    def get_sntp(self) -> SntpModel:
        r = self._session.get(url=self._sntp_base_url)
        validate_200(r)
        return SntpModel(**r.json())


class SntpAsync(SntpBase):
    def __init__(self, session: httpx.AsyncClient):
        super().__init__(session=session)

    async def get_sntp(self) -> SntpModel:
        r = await self._session.get(url=self._sntp_base_url)
        validate_200(r)
        return SntpModel(**r.json())
