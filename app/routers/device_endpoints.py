from fastapi import APIRouter, HTTPException, status
from app.crud.device import get_all_devices, get_device, add_new_device, update_device, delete_device
from app.schemas.schema import DeviceCreateSchema, Date, UpdateDeviceCreateSchema
from app.crud.energy_data import get_device_reading,get_device_reading_on, get_device_reading_range
from datetime import datetime


device_route = APIRouter()

@device_route.post('/devices/', status_code=status.HTTP_201_CREATED)
async def add_device(device: DeviceCreateSchema):
    create_device = add_new_device(device.name, device.id, device.location)
    if not create_device:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Not Created')
    return get_device(device.id)

@device_route.get('/devices/')
async def get_all():
    devices = get_all_devices()
    if not devices:
        raise HTTPException(status_code=404, detail='No Devices Found.')
    return devices

@device_route.get('/devices/{did}')
async def get_one(did: int):
    device = get_device(did)
    if not device:
        raise HTTPException(status_code=404, detail='Device Not Found.')
    return device

@device_route.put('/devices/')
async def update(device: UpdateDeviceCreateSchema):
    info = {"name": device.name, 'location': device.location}
    updated_device = update_device(device.id, info)
    if not updated_device:
        raise HTTPException(status.HTTP_304_NOT_MODIFIED, 'Update Failed')
    return updated_device

@device_route.delete('/device/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: int):
    if not delete_device(id):
        raise HTTPException(status.HTTP_304_NOT_MODIFIED)
    return {'success': True}

@device_route.get('/device/{id}/energy-consumption')
async def get_device_consumption(id: int):
    readings = get_device_reading(id)
    if not readings:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return readings

@device_route.get('/device/{id}/energy_consumption/')
async def get_date_reading(id: int, date: datetime):
    readings = get_device_reading_on(id, date)
    if not readings:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return readings

@device_route.get('/device/{id}/energy_consumption/range')
async def get_range_reading(id: int, start_date: datetime, end_date: datetime = None):
    if end_date and end_date < start_date:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail='End date should be greater than Start date')
    readings = get_device_reading_range(id, start_date, end_date)
    if not readings:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return readings
