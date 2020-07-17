from enum import Enum


class OriginIdEnum(str, Enum):
    NONE = "NONE"
    HOSTNAME = "HOSTNAME"
    IPADDRESS = "IPADDRESS"
