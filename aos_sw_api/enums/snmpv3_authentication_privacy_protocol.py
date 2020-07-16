from enum import Enum


class Snmpv3AuthenticationPrivacyProtocolEnum(str, Enum):
    SAPP_DES = "SAPP_DES"
    SAPP_AES = "SAPP_AES"
    SAPP_NONE = "SAPP_NONE"
