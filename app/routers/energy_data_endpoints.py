from fastapi import APIRouter, HTTPException, status
from app.schemas.schema import EnergyDataSchema
from datetime import datetime
from app.crud.energy_data import *


energy_data_route = APIRouter()

@energy_data_route.get('/energy_consumption')
async def get_all():
    readings = get_readings()
    if not readings:
        raise HTTPException(status.HTTP_204_NO_CONTENT, detail='No Readings Avialiable')
    return readings

@energy_data_route.post('/energy_consumption/', status_code=status.HTTP_201_CREATED)
async def add_new_reading(data: EnergyDataSchema):
    reading = add_reading(data.did, data.voltage, data.current)
    if reading == 0:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail='Invalid Device id')
    if not reading:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)
    return {"success": True}

@energy_data_route.get('/energy_consumption/')
async def get_date_reading(date: datetime):
    readings = get_readings_on(date)
    if not readings:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f'No Availiable data for {date.date()}')
    return readings

@energy_data_route.get('/energy_consumption/range')
async def get_range(start_date: datetime, end_date: datetime | None = None):
    if end_date and end_date < start_date:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail='End date should be greater than or equal to start date')
    data = get_readings_range(start_date, end_date)
    if not data:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f'No Avialiable data between {start_date.date()} and {end_date.date()}.')
    return data

@energy_data_route.get('/energy_consumption/analytics/daily_consumption')
async def get_daily_total(date: datetime):
    total = get_total_daily_consumption(date)
    if not total:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f'No Avialiable data for {date.date()}')
    return total

@energy_data_route.get('/energy_consumption/analytics/total_consumption')
async def get_total():
    total = get_total_consumption()
    if not total:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f'No Avialiable data')
    return total
