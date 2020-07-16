from typing import List

from pydantic import BaseModel, Field

from aos_sw_api.enums import SpanningTreeModeEnum
from aos_sw_api.globel_models import CollectionResult


class SpanningTreeModel(BaseModel):
    is_enabled: bool
    priority: int = Field(..., ge=0, le=15)
    mode: SpanningTreeModeEnum


class SpanningTreePort(BaseModel):
    port_id: str
    priority: int = Field(..., ge=0, le=15)
    is_enable_admin_edge_port: bool
    is_enable_bpdu_protection: bool
    is_enable_bpdu_filter: bool
    is_enable_root_guard: bool


class SpanningTreePortList(BaseModel):
    collection_result: CollectionResult
    stp_port_element: List[SpanningTreePort]
