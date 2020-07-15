from enum import Enum


class PortPoePriorityEnum(str, Enum):
    PPP_CRITICAL = "PPP_CRITICAL"
    PPP_HIGH = "PPP_HIGH"
    PPP_LOW = "PPP_LOW"
