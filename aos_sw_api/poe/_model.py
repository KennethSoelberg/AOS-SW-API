from typing import List

from pydantic import BaseModel, Field

from aos_sw_api.enums import PortPoePriorityEnum, PortPoeAllocationMethodEnum, PortPoeDetectionStatusEnum


class PortPoe(BaseModel):
    port_id: str
    is_poe_enabled: bool
    poe_priority: PortPoePriorityEnum
    poe_allocation_method: PortPoeAllocationMethodEnum
    allocated_power_in_watts: int = Field(..., ge=1, le=33)
    port_configured_type: str = Field(..., max_length=256)
    pre_standard_detect_enabled: bool


class PortPoeStats(BaseModel):
    port_id: str
    poe_detection_status: PortPoeDetectionStatusEnum
    port_voltage_in_volts: int
    power_denied_count: int
    over_current_count: int
    mps_absent_count: int
    short_count: int
    actual_power_in_watts: int
    power_class: int


class PortPoeList(BaseModel):
    port_poe: List[PortPoe]


class PortPoeStatsList(BaseModel):
    port_poe_stats: List[PortPoeStats]
