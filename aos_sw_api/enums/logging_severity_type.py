from enum import Enum


class LoggingSeverityTypeEnum(str, Enum):
    MAJOR = "MAJOR"
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"
    DEBUG = "DEBUG"

