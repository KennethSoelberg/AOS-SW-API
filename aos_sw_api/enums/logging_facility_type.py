from enum import Enum


class LoggingFacilityTypeEnum(str, Enum):
    KERN = "KERN"
    USER = "USER"
    MAIL = "MAIL"
    DAEMON = "DAEMON"
    AUTH = "AUTH"
    SYSLOG = "SYSLOG"
    LPR = "LPR"
    NEWS = "NEWS"
    UUCP = "UUCP"
    SYS9 = "SYS9"
    SYS10 = "SYS10"
    SYS11 = "SYS11"
    SYS12 = "SYS12"
    SYS13 = "SYS13"
    SYS14 = "SYS14"
    CRON = "CRON"
    LOCAL0 = "LOCAL0"
    LOCAL1 = "LOCAL1"
    LOCAL2 = "LOCAL2"
    LOCAL3 = "LOCAL3"
    LOCAL4 = "LOCAL4"
    LOCAL5 = "LOCAL5"
    LOCAL6 = "LOCAL6"
    LOCAL7 = "LOCAL7"

