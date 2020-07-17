from typing import Union

import httpx

from aos_sw_api.validate import validate_200
from ._model import CliCommandResult


class CliCommand:

    def __new__(cls, session: Union[httpx.Client, httpx.AsyncClient], **kwargs):
        if isinstance(session, httpx.Client):
            return CliCommandSync(session=session)
        elif isinstance(session, httpx.AsyncClient):
            return CliCommandAsync(session=session)


class CliCommandBase:
    def __init__(self, session: Union[httpx.Client, httpx.AsyncClient]):
        self._session = session
        self._cli_base_url = "cli"


class CliCommandSync(CliCommandBase):
    def __init__(self, session: httpx.Client):
        super().__init__(session=session)

    def send_command(self, cmd: str) -> CliCommandResult:
        data = {"cmd": cmd}
        r = self._session.post(url=self._cli_base_url, json=data)
        validate_200(r)
        return CliCommandResult(**r.json())


class CliCommandAsync(CliCommandBase):
    def __init__(self, session: httpx.AsyncClient):
        super().__init__(session=session)

    async def send_command(self, cmd: str) -> CliCommandResult:
        data = {"cmd": cmd}
        r = await self._session.post(url=self._cli_base_url, json=data)
        validate_200(r)
        return CliCommandResult(**r.json())
