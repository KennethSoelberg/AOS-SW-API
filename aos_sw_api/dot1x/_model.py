from typing import List

from pydantic import BaseModel, Field

from aos_sw_api.enums import Dot1xAuthenticatorPortControlEnum, Dot1xControlledDirectionEnum
from aos_sw_api.globel_models import CollectionResult


class Dot1xModel(BaseModel):
    is_dot1x_enabled: bool
    cached_reauth_delay: int = Field(..., ge=0, le=2147483647)
    allow_gvrp_vlans: bool
    use_lldp_data: bool


class Dot1xAuthenticatorPort(BaseModel):
    port_id: str
    is_authenticator_enabled: bool
    control: Dot1xAuthenticatorPortControlEnum
    unauthorized_vlan_id: int = Field(..., ge=0, le=4094)
    client_limit: int = Field(..., ge=0, le=32)
    quiet_period: int = Field(..., ge=0, le=65535)
    tx_period: int = Field(..., ge=1, le=65535)
    supplicant_timeout: int = Field(..., ge=1, le=300)
    server_timeout: int = Field(..., ge=1, le=300)
    max_requests: int = Field(..., ge=1, le=10)
    reauth_period: int = Field(..., ge=0, le=999999999)
    authorized_vlan_id: int = Field(..., ge=0, le=4094)
    logoff_period: int = Field(..., ge=1, le=999999999)
    unauth_period: int = Field(..., ge=0, le=250)
    cached_reauth_period: int = Field(..., ge=0, le=2147483647)


class Dot1xPortSecurity(BaseModel):
    port_id: str
    controlled_direction: Dot1xControlledDirectionEnum
    allow_mbv: bool
    allowed_mixed_users: bool
    is_port_speed_vsa_enabled: bool


class Dot1xAuthenticatorPortList(BaseModel):
    collection_result: CollectionResult
    dot1x_authenticator_port_element: List[Dot1xAuthenticatorPort]


class Dot1xPortSecurityList(BaseModel):
    collection_result: CollectionResult
    dot1x_port_security_element: List[Dot1xPortSecurity]
