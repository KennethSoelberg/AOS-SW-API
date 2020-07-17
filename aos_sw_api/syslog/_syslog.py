from typing import Union

import httpx

from aos_sw_api.validate import validate_200
from ._model import SyslogModel


class Syslog:

    def __new__(cls, session: Union[httpx.Client, httpx.AsyncClient], **kwargs):
        if isinstance(session, httpx.Client):
            return SyslogSync(session=session)
        elif isinstance(session, httpx.AsyncClient):
            return SyslogAsync(session=session)


class SyslogBase:
    def __init__(self, session: Union[httpx.Client, httpx.AsyncClient]):
        self._session = session
        self._syslog_base_url = "syslog"


class SyslogSync(SyslogBase):
    def __init__(self, session: httpx.Client):
        super().__init__(session=session)

    def get_syslog(self) -> SyslogModel:
        r = self._session.get(url=self._syslog_base_url)
        validate_200(r)
        return SyslogModel(**r.json())


class SyslogAsync(SyslogBase):
    def __init__(self, session: httpx.AsyncClient):
        super().__init__(session=session)

    async def get_syslog(self) -> SyslogModel:
        r = await self._session.get(url=self._syslog_base_url)
        validate_200(r)
        return SyslogModel(**r.json())
