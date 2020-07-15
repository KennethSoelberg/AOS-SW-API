from enum import Enum


class PortModeEnum(str, Enum):
    POM_UNTAGGED = "POM_UNTAGGED"
    POM_TAGGED_STATIC = "POM_TAGGED_STATIC"
    POM_FORBIDDEN = "POM_FORBIDDEN"
