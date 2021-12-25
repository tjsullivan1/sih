from typing import Optional
from pydantic import BaseModel

from datetime import datetime
from models.location import Location

class TenantSubmittal(BaseModel):
    first_name: str
    last_name: str
    email_address: str
    phone_number: int
    business_name: Optional[str]
    billing_address: Location


class Tenant(TenantSubmittal):
    id: str
    created_date: Optional[datetime]
