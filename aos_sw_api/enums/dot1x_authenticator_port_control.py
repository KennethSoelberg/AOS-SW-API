from enum import Enum


class Dot1xAuthenticatorPortControlEnum(str, Enum):
    DAPC_UNAUTHORIZED = "DAPC_UNAUTHORIZED"
    DAPC_AUTO = "DAPC_AUTO"
    DAPC_AUTHORIZED = "DAPC_AUTHORIZED"
