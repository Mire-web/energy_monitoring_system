#!/usr/bin/python3
"""
Description: Crud operations for energy data manipulation
"""
from crud import Session
from datetime import datetime
from db.setup import Energy_data
from db.setup import Device
from sqlalchemy import func


session = Session()

# Add new reading from device
def add_reading(did: int, volts: float, current: float):
    new_reading = Energy_data(
		device_id = did,
        voltage = round(volts, 4),
        current = round(current, 4),
        power = round(volts * current, 4),
        timestamp = datetime.now()
	)
    session.add(new_reading)
    try:
        session.commit()
        return True
    except Exception as e:
        # TODO: log error to file
        session.rollback()
        return False

# Get readings for specific device
def get_device_reading(did: int):
    device_reading = session.query(Device).filter_by(id=did).first()
    if device_reading:
        return device_reading.energy_consumption
    else:
        return None

# Get all readings
def get_readings():
    energy_reading = session.query(Energy_data).all()
    if energy_reading:
        return energy_reading
    else:
        return None

# Get device readings filtered by date
def get_device_reading_on(did: int, date: datetime):
    device_reading = session.query(
        Energy_data).filter(
            Energy_data.device_id==did).filter(
                func.date(
                    Energy_data.timestamp) >= date.date()).all()
    if device_reading:
        return device_reading
    else:
        return None

# Get device readings filtered by date
def get_readings_on(date: datetime):
    readings = session.query(Energy_data).filter(func.date(Energy_data.timestamp) >= date.date()).all()
    if readings:
        return readings
    else:
        return None

# Get daily consumption
def get_total_daily_consumption(date: datetime):
    day_readings = session.query(Energy_data).with_entities(
        Energy_data.voltage, Energy_data.current).filter(
            func.date(Energy_data.timestamp) == date.date()).all()
    if day_readings:
        total_voltage = 0
        total_current = 0
        total_power = 0
        for voltage, current in day_readings:
            total_voltage += voltage
            total_current += current
            total_power += voltage * current
        return {'voltage': f'{total_voltage:.4f}V',
                'current': f'{total_current:.4f}A',
                'power': f'{total_power/1000:.4f}kW'}
    else:
        return None

# Get total consumption aggregated
def get_aggregate_consumption():
    readings = session.query(Energy_data).with_entities(
        Energy_data.voltage, Energy_data.current).all()
    if readings:
        total_voltage = 0
        total_current = 0
        total_power = 0
        for voltage, current in readings:
            total_voltage += voltage
            total_current += current
            total_power += voltage * current
        return {'voltage': f'{total_voltage:.4f}V',
                'current': f'{total_current:.4f}A',
                'power': f'{total_power/1000:.4f}kW'}
    else:
        return None
