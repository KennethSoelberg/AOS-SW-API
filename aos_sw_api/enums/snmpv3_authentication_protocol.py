from enum import Enum


class Snmpv3AuthenticationProtocolEnum(str, Enum):
    SAP_MD5 = "SAP_MD5"
    SAP_SHA = "SAP_SHA"
    SAP_NONE = "SAP_NONE"
