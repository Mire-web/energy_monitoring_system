#!/usr/bin/python3
"""
Description: Crud operations for energy data manipulation
"""
from app.crud import Session
from datetime import datetime
from app.db.setup import Energy_data
from app.db.setup import Device
from sqlalchemy import func


session = Session()

# Add new reading from device
def add_reading(did: int, volts: float, current: float):
    device = session.query(Device).filter(Device.id == did).first()
    if not device:
        return 0
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
    energy_reading = session.query(Energy_data).join(Device, Energy_data.device_id == Device.id).order_by(Energy_data.id).all()
    energy_reading = [reading.as_dict() for reading in energy_reading]
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
        Energy_data.timestamp) == date.date()).join(
        Device, Energy_data.device_id == Device.id).order_by(
        Energy_data.id).all()
    device_reading = [reading.as_dict() for reading in device_reading]
    if device_reading:
        return device_reading
    else:
        return None


# Get device readings filtered by date
def get_device_reading_range(did: int, start_date: datetime, end_date: datetime):
    if end_date:
        device_reading = session.query(
            Energy_data).filter(
            Energy_data.device_id==did).filter(
            (func.date(
            Energy_data.timestamp) >= start_date.date()) & (func.date(Energy_data.timestamp) <= end_date.date())).join(
            Device, Energy_data.device_id == Device.id).order_by(
            Energy_data.id).all()
    else:
        device_reading = session.query(
            Energy_data).filter(
            Energy_data.device_id==did).filter(
            func.date(
            Energy_data.timestamp) >= start_date.date()).join(
            Device, Energy_data.device_id == Device.id).order_by(
            Energy_data.id).all()
    device_readings = [reading.as_dict() for reading in device_reading]
    print(device_readings)
    if device_readings:
        return device_readings
    else:
        return None


# Get readings filtered by date
def get_readings_on(date: datetime):
    readings = session.query(Energy_data).filter(func.date(Energy_data.timestamp) == date.date()).join(Device, Energy_data.device_id == Device.id).all()
    readings = [reading.as_dict() for reading in readings]
    if readings:
        return readings
    else:
        return None
    
# Get Readings filtered by range
def get_readings_range(start_date: datetime, end_date: datetime):
    if end_date:
        readings = session.query(
            Energy_data
            ).filter(
		    (func.date(Energy_data.timestamp) >= start_date.date()) & (func.date(Energy_data.timestamp) <= end_date.date())
	        ).join(
            Device, Energy_data.device_id == Device.id
            ).order_by(
            Energy_data.id).all()
    else:
        readings = session.query(
            Energy_data
            ).filter(
		    (func.date(Energy_data.timestamp) >= start_date.date())
	        ).join(
            Device, Energy_data.device_id == Device.id
            ).order_by(
            Energy_data.id
            ).all()
    readings = [reading.as_dict() for reading in readings]
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
def get_total_consumption():
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
                'power': f'{total_power:.4f}W'}
    else:
        return None

# Get device total
def get_device_day_consumption(model: int, date: datetime.date):
    readings = session.query(Energy_data).with_entities(Device.name, Energy_data.voltage, Energy_data.current).filter((Energy_data.id == model & func.date(Energy_data.timestamp == date))).join(Device, Energy_data.id == Device.id).all()
    if readings:
        total_voltage = 0
        total_current = 0
        total_power = 0
        for data in readings:
            total_voltage += data.voltage
            total_current += data.current
            total_power += total_voltage * total_current
        return {'name': Device.name,
                'voltage': f'{total_voltage:.4f}V',
                'current': f'{total_current:.4f}A',
                'power': f'{total_power:.4f}W'}
    else:
        return None
# Get device total within range
def get_device_total_within(model: int, startDate: datetime.date, endDate: datetime.date):
    readings = session.query(Energy_data).with_entities(Device.name, Energy_data.voltage, Energy_data.current).filter((Energy_data.id == model & (func.date(Energy_data.timestamp == startDate) & func.date(Energy_data.timestamp == endDate)))).join(Device, Energy_data.id == Device.id).all()
    if readings:
        total_voltage = 0
        total_current = 0
        total_power = 0
        for data in readings:
            total_voltage += data.voltage
            total_current += data.current
            total_power += total_voltage * total_current
        return {'name': Device.name,
                'voltage': f'{total_voltage:.4f}V',
                'current': f'{total_current:.4f}A',
                'power': f'{total_power:.4f}W'}

# Get total within range
def get_total_within(startDate: datetime.date, endDate: datetime.date):
    readings = session.query(Energy_data).with_entities(Device.name, Energy_data.voltage, Energy_data.current).filter(((func.date(Energy_data.timestamp == startDate) & func.date(Energy_data.timestamp == endDate)))).join(Device, Energy_data.id == Device.id).all()
    if readings:
        total_voltage = 0
        total_current = 0
        total_power = 0
        for data in readings:
            total_voltage += data.voltage
            total_current += data.current
            total_power += total_voltage * total_current
        return {'name': Device.name,
                'voltage': f'{total_voltage:.4f}V',
                'current': f'{total_current:.4f}A',
                'power': f'{total_power:.4f}W'}
