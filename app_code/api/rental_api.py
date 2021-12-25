from typing import Optional, List
import fastapi
from fastapi import Depends
from models.tenant import Tenant, TenantSubmittal
from models.validation_error import ValidationError
from models.location import Location
from services import tenant_service

router = fastapi.APIRouter()

@router.get('/api/tenants', name='all_tenants', response_model=List[Tenant])
async def tenants_get() -> List[Tenant]:

    return await tenant_service.get_tenants()


@router.post('/api/tenants', name='add_tenant', status_code=201, response_model=Tenant)
async def tenants_post(tenant_submittal: TenantSubmittal) -> Tenant:
    bill = tenant_submittal.billing_address
    first_name = tenant_submittal.first_name
    last_name = tenant_submittal.last_name
    phone_number = tenant_submittal.phone_number
    email_address = tenant_submittal.email_address
    business_name = tenant_submittal.business_name

    return await tenant_service.add_tenant(first_name, last_name, email_address, phone_number, bill, business_name)