from enum import Enum


class PortPoeAllocationMethodEnum(str, Enum):
    PPAM_USAGE = "PPAM_USAGE"
    PPAM_CLASS = "PPAM_CLASS"
    PPAM_VALUE = "PPAM_VALUE"
