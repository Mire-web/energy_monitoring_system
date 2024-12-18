#!/usr/bin/python3
"""
Main app script
"""
from fastapi import FastAPI
from app.routers.device_endpoints import device_route
from app.routers.energy_data_endpoints import energy_data_route


app = FastAPI()

@app.get('/')
def home():
    return 'Welcome to Curon energy monitoring system'

app.include_router(device_route)
app.include_router(energy_data_route)
