from pydantic import BaseModel

from aos_sw_api.enums import CliCmdStatusEnum


class CliCommandResult(BaseModel):
    cmd: str
    result_base64_encoded: str
    error_msg: str
    status: CliCmdStatusEnum
