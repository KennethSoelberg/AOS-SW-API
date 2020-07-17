from typing import List

from pydantic import BaseModel

from aos_sw_api.globel_models import CollectionResult, MacAddress


class MacTableEntry(BaseModel):
    mac_address: str
    vlan_id: int
    port_id: str


class MacTableEntryList(BaseModel):
    collection_result: CollectionResult
    mac_table_entry_element: List[MacTableEntry]
