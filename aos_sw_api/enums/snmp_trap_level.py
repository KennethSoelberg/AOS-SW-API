from enum import Enum


class SnmpTrapLevelEnum(str, Enum):
    STL_ALL = "STL_ALL"
    STL_CRITICAL = "STL_CRITICAL"
    STL_NOT_INFO = "STL_NOT_INFO"
    STL_DEBUG = "STL_DEBUG"
    STL_NONE = "STL_NONE"
