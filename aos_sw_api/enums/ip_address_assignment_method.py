from enum import Enum


class IpAddressAssignmentMethodEnum(str, Enum):
    IAAM_DISABLED = "IAAM_DISABLED"
    IAAM_STATIC = "IAAM_STATIC"
    IAAM_DHCP = "IAAM_DHCP"
