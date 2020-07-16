from pydantic import BaseModel


class CollectionResult(BaseModel):
    total_elements_count: int
    filtered_elements_count: int
