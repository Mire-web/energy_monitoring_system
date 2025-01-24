from fastapi import APIRouter, HTTPException, status
from datetime import datetime
from app.crud.alert import *


alert_route = APIRouter()

@alert_route.get('/alerts/history', status_code=status.HTTP_200_OK)
async def get_all():
    response = get_alerts()
    if not response:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='No Alerts')
    return response

@alert_route.post('/alerts/history/{did}', status_code=status.HTTP_200_OK)
async def post_alert(did: int, parameter=None, trigger_value=None):
    if not parameter or not trigger_value:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Parameter and Trigger value cannot be empty')
    response = add_alert_to_history(did, parameter, float(trigger_value))
    if response != True:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=response)
    return response

@alert_route.get('/alerts/{did}/history', status_code=status.HTTP_200_OK)
async def get_device_alerts(did: int, parameter=None, startDate:datetime =None, endDate: datetime =None):
    response = get_device_alert_history(did, parameter, startDate, endDate)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return response

@alert_route.post('/{did}/alerts/', status_code=status.HTTP_200_OK)    
async def add_limitt(did: int, param: str=None, threshold: float=None):
    if not param or not threshold:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='param and threshold cannot be empty')
    response = add_limit(did, param, threshold)
    if not response:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error try again")
    return response

@alert_route.get('/{did}/alerts/', status_code=status.HTTP_200_OK)
async def get_limit_device(did: int, parameter: str=None):
    response = get_device_limit(did, parameter)
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return response

@alert_route.put('/{did}/alerts/', status_code=status.HTTP_200_OK)
async def update_limit(did: int, param: str=None, value: float=None):
    if not param or not value:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Param and Value cannot be empty')
    response = update_device_limit(did, param, value)
    if response != True:
        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED, detail=response)
    return response

@alert_route.get('/alerts/', status_code=status.HTTP_200_OK)
async def get_limits():
    response = get_alert_thresholds()
    if not response:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return response
