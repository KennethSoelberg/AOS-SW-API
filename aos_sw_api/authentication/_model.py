from pydantic import BaseModel

from aos_sw_api.enums import PrimaryAuthMethodEnum, SecondaryAuthMethodEnum


class AuthenticationLoginConfig(BaseModel):
    primary_method: PrimaryAuthMethodEnum
    secondary_method: SecondaryAuthMethodEnum


class AuthenticationModel(BaseModel):
    is_privilege_mode_enabled: bool


class AuthenticationConsole(BaseModel):
    auth_console_login: AuthenticationLoginConfig


class AuthenticationSsh(BaseModel):
    auth_ssh_login: AuthenticationLoginConfig
