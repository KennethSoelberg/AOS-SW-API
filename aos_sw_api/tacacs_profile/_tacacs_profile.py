from typing import Union

import httpx

from aos_sw_api.validate import validate_200
from ._model import TacacsProfileModel


class TacacsProfile:

    def __new__(cls, session: Union[httpx.Client, httpx.AsyncClient], **kwargs):
        if isinstance(session, httpx.Client):
            return TacacsProfileSync(session=session)
        elif isinstance(session, httpx.AsyncClient):
            return TacacsProfileAsync(session=session)


class TacacsProfileBase:
    def __init__(self, session: Union[httpx.Client, httpx.AsyncClient]):
        self._session = session
        self._tacacs_profile_base_url = "tacacs_profile"


class TacacsProfileSync(TacacsProfileBase):
    def __init__(self, session: httpx.Client):
        super().__init__(session=session)

    def get_tacacs_profile(self) -> TacacsProfileModel:
        r = self._session.get(url=self._tacacs_profile_base_url)
        validate_200(r)
        return TacacsProfileModel(**r.json())


class TacacsProfileAsync(TacacsProfileBase):
    def __init__(self, session: httpx.AsyncClient):
        super().__init__(session=session)

    async def get_tacacs_profile(self) -> TacacsProfileModel:
        r = await self._session.get(url=self._tacacs_profile_base_url)
        validate_200(r)
        return TacacsProfileModel(**r.json())
