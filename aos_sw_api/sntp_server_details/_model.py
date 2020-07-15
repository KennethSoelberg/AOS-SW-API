from typing import List

from pydantic import BaseModel, Field

from aos_sw_api.globel_models import IpAddressModel


class SntpServerDetailsModel(BaseModel):
    sntp_server_address: IpAddressModel
    sntp_server_priority: int = Field(..., ge=1, le=3)
    sntp_server_version: int = Field(..., ge=1, le=7)
    sntp_server_is_oobm: bool


class SntpServerDetailsList(BaseModel):
    sntp_servers: List[SntpServerDetailsModel]
