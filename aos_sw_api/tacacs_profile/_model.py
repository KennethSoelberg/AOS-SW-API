from typing import List

from pydantic import BaseModel, Field

from aos_sw_api.globel_models import IpAddressModel


class TacacsServer(BaseModel):
    server_ip: IpAddressModel
    auth_key: str = Field(..., max_length=100)
    is_oobm: bool = Field(None, description="not on switch without oobm")


class TacacsProfileModel(BaseModel):
    tacacs_servers: List[TacacsServer]
    dead_time: int = Field(..., ge=0, le=1440)
    time_out: int = Field(..., ge=1, le=255)
    source_ip_select: str = Field(None, description="Not on 2620 and 3800")
    global_auth_key: str = Field(..., max_length=100)
