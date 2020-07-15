from typing import List

from pydantic import BaseModel, Field

from aos_sw_api.enums import VlanStatusEnum, VlanTypeEnum


class VlanModel(BaseModel):
    vlan_id: int = Field(..., ge=1, le=4094)
    name: str = Field(..., max_length=32)
    status: VlanStatusEnum
    type: VlanTypeEnum
    is_voice_enabled: bool
    is_jumbo_enabled: bool
    is_dsnoop_enabled: bool
    is_dhcp_server_enabled: bool = Field(None, description="Not on 2620 and 2530")
    is_primary_vlan: bool = Field(None, description="not on 2620 and 3800")


class VlanList(BaseModel):
    vlan_element: List[VlanModel]
