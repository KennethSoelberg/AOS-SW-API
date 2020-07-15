from typing import List

from pydantic import BaseModel, Field

from aos_sw_api.enums import IpAddressAssignmentMethodEnum
from aos_sw_api.globel_models import IpAddressModel


class IpAddressSubnetModel(BaseModel):
    vlan_id: int = Field(..., ge=1, le=4094)
    ip_address_mode: IpAddressAssignmentMethodEnum
    ip_address: IpAddressModel
    ip_mask: IpAddressModel


class IpAddressSubnetList(BaseModel):
    ip_address_subnet_element: List[IpAddressSubnetModel]
