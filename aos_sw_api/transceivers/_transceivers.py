from typing import Union

import httpx

from aos_sw_api.validate import validate_200
from ._model import TransceiverList


class Transceiver:

    def __new__(cls, session: Union[httpx.Client, httpx.AsyncClient], **kwargs):
        if isinstance(session, httpx.Client):
            return TransceiverSync(session=session)
        elif isinstance(session, httpx.AsyncClient):
            return TransceiverAsync(session=session)


class TransceiverBase:
    def __init__(self, session: Union[httpx.Client, httpx.AsyncClient]):
        self._session = session
        self._transceivers_base_url = "transceivers"


class TransceiverSync(TransceiverBase):
    def __init__(self, session: httpx.Client):
        super().__init__(session=session)

    def get_transceivers(self) -> TransceiverList:
        r = self._session.get(url=self._transceivers_base_url)
        validate_200(r)
        return TransceiverList(**r.json())


class TransceiverAsync(TransceiverBase):
    def __init__(self, session: httpx.AsyncClient):
        super().__init__(session=session)

    async def get_transceivers(self) -> TransceiverList:
        r = await self._session.get(url=self._transceivers_base_url)
        validate_200(r)
        return TransceiverList(**r.json())

