from enum import Enum


class SntpClientOperationModeEnum(str, Enum):
    SNTP_DISABLE = "SNTP_DISABLE"
    SNTP_UNICAST_MODE = "SNTP_UNICAST_MODE"
    SNTP_BROADCAST_MODE = "SNTP_BROADCAST_MODE"
    SNTP_DHCP_MODE = "SNTP_DHCP_MODE"
