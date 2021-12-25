from pydantic import BaseModel
from typing import Optional

class Location(BaseModel):
    street_address1: str
    street_address2: Optional[str] = None
    city: str
    state: str
    zip_code: int
    country: Optional[str] = 'US'
