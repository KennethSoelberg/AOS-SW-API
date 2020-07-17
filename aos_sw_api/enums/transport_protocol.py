from enum import Enum


class TransportProtocolEnum(str, Enum):
    TP_UDP = "TP_UDP"
    TP_TCP = "TP_TCP"
    TP_TLS = "TP_TLS"
