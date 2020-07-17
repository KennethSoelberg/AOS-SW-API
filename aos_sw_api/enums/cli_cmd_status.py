from enum import Enum


class CliCmdStatusEnum(str, Enum):
    CCS_SUCCESS = "CCS_SUCCESS"
    CCS_FAILURE = "CCS_FAILURE"
