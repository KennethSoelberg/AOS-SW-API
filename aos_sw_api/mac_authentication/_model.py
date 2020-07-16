from typing import List

from pydantic import BaseModel, Field

from aos_sw_api.globel_models import CollectionResult


class MacAuthenticationModel(BaseModel):
    unauthorized_vlan_id: int = Field(..., ge=0, le=4094)


class MacAuthenticationPort(BaseModel):
    port_id: str
    is_mac_authentication_enabled: bool
    reauthenticate: bool
    mac_address_limit: int = Field(..., ge=1, le=256)
    unauthorized_vlan_id: int = Field(..., ge=0, le=4094)


class MacAuthenticationPortList(BaseModel):
    collection_result: CollectionResult
    mac_authentication_port_element: List[MacAuthenticationPort]
