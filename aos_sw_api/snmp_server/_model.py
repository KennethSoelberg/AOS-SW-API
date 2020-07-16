from typing import List

from pydantic import BaseModel, Field

from aos_sw_api.enums import UserTypeEnum, SnmpTrapLevelEnum, SnmpTrapModeEnum, SnmpAuthTrapModeEnum
from aos_sw_api.globel_models import CollectionResult, IpAddressModel


class SnmpServerModel(BaseModel):
    is_snmp_server_enabled: bool
    local_engine_id: str


class SnmpServerCommunity(BaseModel):
    access_type: UserTypeEnum
    community_name: str
    restricted: bool


class SnmpServerCommunityList(BaseModel):
    collection_result: CollectionResult
    snmp_server_community_element: List[SnmpServerCommunity]


class SnmpServerHost(BaseModel):
    host_ip: IpAddressModel
    community: str
    trap_level: SnmpTrapLevelEnum
    informs: bool
    inform_timeout: int = Field(..., ge=1, le=21474836)
    inform_retries: int = Field(..., ge=0, le=255)
    use_oobm: bool = Field(None, description="not on 2530 and 2620")


class SnmpServerHostList(BaseModel):
    collection_result: CollectionResult
    snmp_server_host_element: List[SnmpServerHost]


class SnmpServerRunConfTrap(BaseModel):
    running_conf_change_trap: SnmpTrapModeEnum
    trap_interval: int = Field(..., ge=0, le=2147483647)


class SnmpServerMacNotifyTrap(BaseModel):
    mac_move_notify_mode: SnmpTrapModeEnum
    trap_interval: int = Field(..., ge=0, le=120)
    mac_notify_mode: SnmpTrapModeEnum


class SnmpServerTraps(BaseModel):
    arp_protect: SnmpTrapModeEnum
    auth_server_fail: SnmpTrapModeEnum
    dhcp_server: SnmpTrapModeEnum = Field(None, description="Not on 2530")
    dhcp_snooping: SnmpTrapModeEnum
    dhcpv6_snooping_errant_replies: SnmpTrapModeEnum
    dhcpv6_snooping_out_of_resource: SnmpTrapModeEnum
    dyn_ip_lockdown: SnmpTrapModeEnum
    dyn_ipv6_ld_out_of_resources: SnmpTrapModeEnum
    dyn_ipv6_ld_violations: SnmpTrapModeEnum
    login_failure_mgr: SnmpTrapModeEnum
    mac_count_notify: SnmpTrapModeEnum
    nd_snooping_out_of_resources: SnmpTrapModeEnum = Field(None, description="Not on 2530 and 2620")
    password_change_mgr: SnmpTrapModeEnum
    port_security: SnmpTrapModeEnum
    startup_config_change: SnmpTrapModeEnum
    snmp_authentication: SnmpAuthTrapModeEnum
    mac_notify: SnmpServerMacNotifyTrap
    running_config_changes: SnmpServerRunConfTrap
