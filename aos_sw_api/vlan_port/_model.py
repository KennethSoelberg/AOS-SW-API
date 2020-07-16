from typing import List

from pydantic import BaseModel, Field

from aos_sw_api.enums import PortModeEnum
from aos_sw_api.globel_models import CollectionResult


class VlanPortModel(BaseModel):
    vlan_id: int = Field(..., ge=1, le=4094)
    port_id: str
    port_mode: PortModeEnum


class VlanPortList(BaseModel):
    collection_result: CollectionResult
    vlan_port_element: List[VlanPortModel]
