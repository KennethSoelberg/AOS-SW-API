from typing import List

from pydantic import BaseModel, Field

from aos_sw_api.enums import TimeWindowTypeEnum
from aos_sw_api.globel_models import IpAddressModel, CollectionResult


class RadiusServerModel(BaseModel):
    radius_server_id: int = Field(..., ge=1, le=15)
    address: IpAddressModel
    shared_secret: str = Field(..., max_length=32)
    authentication_port: int = Field(..., ge=1, le=65535)
    accounting_port: int = Field(..., ge=1, le=65535)
    is_dyn_authorization_enabled: bool
    time_window_type: TimeWindowTypeEnum
    time_window: int = Field(..., ge=0, le=65535)
    is_oobm: bool = Field(None, description="only switch with oobm")
    is_clearpass_server: bool = Field(None, description="Not on 2620 and 2530")


class RadiusServerList(BaseModel):
    collection_result: CollectionResult
    radius_server_element: List[RadiusServerModel]
