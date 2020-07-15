from enum import Enum


class PrimaryAuthMethodEnum(str, Enum):
    PAM_LOCAL = "PAM_LOCAL"
    PAM_TACACS = "PAM_TACACS"
    EMPTY = ""  #Bug in switch api missing enums Radius
