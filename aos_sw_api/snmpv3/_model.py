from typing import List

from pydantic import BaseModel, Field

from aos_sw_api.enums import Snmpv3AuthenticationProtocolEnum, Snmpv3AuthenticationPrivacyProtocolEnum
from aos_sw_api.enums import Snmpv3GroupTypeEnum
from aos_sw_api.globel_models import CollectionResult


class SnmpV3Model(BaseModel):
    is_snmpv3_server_enabled: bool
    is_non_snmpv3_access_readonly: bool
    is_snmpv3_messages_only: bool


class SnmpV3User(BaseModel):
    user_name: str = Field(..., max_length=32)
    snmpv3_authentication_protocol: Snmpv3AuthenticationProtocolEnum
    snmpv3_authentication_privacy_protocol: Snmpv3AuthenticationPrivacyProtocolEnum
    authentication_password: str = Field(..., min_length=6, max_length=32)
    privacy_password: str = Field(..., min_length=6, max_length=32)
    snmpv3_v1_group: Snmpv3GroupTypeEnum
    snmpv3_v2c_group: Snmpv3GroupTypeEnum
    snmpv3_v3_group: Snmpv3GroupTypeEnum


class SnmpV3UserList(BaseModel):
    collection_result: CollectionResult
    snmpv3_user_element: List[SnmpV3User]
