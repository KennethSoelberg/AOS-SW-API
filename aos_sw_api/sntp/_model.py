from pydantic import BaseModel, Field

from aos_sw_api.enums import SntpClientOperationModeEnum


class SntpModel(BaseModel):
    sntp_client_operation_mode: SntpClientOperationModeEnum
    sntp_config_poll_interval: int = Field(..., ge=30, le=720)
