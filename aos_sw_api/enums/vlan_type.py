from enum import Enum


class VlanTypeEnum(str, Enum):
    VT_STATIC = "VT_STATIC"
    VT_STATIC_SVLAN = "VT_STATIC_SVLAN"
    VT_GVRP = "VT_GVRP"
