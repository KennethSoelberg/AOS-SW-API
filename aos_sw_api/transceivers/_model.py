from typing import List

from pydantic import BaseModel

from aos_sw_api.globel_models import CollectionResult


class Transceiver(BaseModel):
    port_id: str
    type: str
    product_number: str
    serial_number: str
    part_number: str
    message: str

class TransceiverList(BaseModel):
    collection_result: CollectionResult
    transceiver_element: List[Transceiver]
