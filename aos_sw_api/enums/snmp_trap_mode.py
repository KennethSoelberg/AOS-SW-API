from enum import Enum


class SnmpTrapModeEnum(str, Enum):
    STM_ENABLE = "STM_ENABLE"
    STM_DISABLE = "STM_DISABLE"
    STM_NONE = "STM_NONE"
