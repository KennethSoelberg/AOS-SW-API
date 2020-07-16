from enum import Enum


class SnmpAuthTrapModeEnum(str, Enum):
    SATM_EXTENDED = "SATM_EXTENDED"
    SATM_STANDARD = "SATM_STANDARD"
    STM_NONE = "STM_NONE"
