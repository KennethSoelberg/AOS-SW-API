from typing import List

from pydantic import BaseModel, Field

from aos_sw_api.enums import PortModeEnum


class VlanPortModel(BaseModel):
    vlan_id: int = Field(..., ge=1, le=4094)
    port_id: str
    port_mode: PortModeEnum


class VlanPortList(BaseModel):
    vlan_port_element: List[VlanPortModel]
