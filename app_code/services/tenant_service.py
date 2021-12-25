from datetime import datetime
from typing import List
from models.location import Location
from models.tenant import Tenant
import uuid

__tenants = []

async def get_tenants() -> List[Tenant]:
    # would add an async call here.
    return list(__tenants)


async def add_tenant(first_name: str, last_name: str, email_address: str, phone_number: int, billing_address: Location, business_name=None) -> Tenant:
    now = datetime.now()
    tenant = Tenant(id=str(uuid.uuid4()), billing_address=billing_address, first_name=first_name, last_name=last_name, phone_number=phone_number, email_address=email_address, business_name=business_name, created_date=now)

    # would add an async call here
    __tenants.append(tenant)
    __tenants.sort(key=lambda r: r.created_date, reverse=True)

    return tenant
