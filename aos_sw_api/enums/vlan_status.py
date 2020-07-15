from enum import Enum


class VlanStatusEnum(str, Enum):
    VS_PORT_BASED = "VS_PORT_BASED"
    VS_PROTOCOL_BASED = "VS_PROTOCOL_BASED"
    VS_DYNAMIC = "VS_DYNAMIC"
