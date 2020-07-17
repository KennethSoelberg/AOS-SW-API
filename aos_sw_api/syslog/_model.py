from typing import List

from pydantic import BaseModel, Field

from aos_sw_api.enums import LoggingSystemModuleTypeEnum, LoggingSeverityTypeEnum, LoggingFacilityTypeEnum
from aos_sw_api.enums import OriginIdEnum, TransportProtocolEnum
from aos_sw_api.globel_models import IpAddressModel


class SyslogServer(BaseModel):
    ip_address: IpAddressModel
    transport_protocol: TransportProtocolEnum
    port: int = Field(..., ge=1, le=49151)
    is_oobm: bool = Field(None, description="not on 2620 and 2530")


class SyslogModel(BaseModel):
    severity: LoggingSeverityTypeEnum
    facility: LoggingFacilityTypeEnum
    system_module: LoggingSystemModuleTypeEnum
    notify_running_config_change: bool
    transmission_interval: int = Field(..., ge=0, le=4294967295)
    priority_descr: str = Field(..., max_length=255)
    origin_id: OriginIdEnum
    servers: List[SyslogServer]
