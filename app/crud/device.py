#!/usr/bin/python3
"""
Description: Crud operations for device
"""
from crud import Session
from db.setup import Device


session = Session()
# Add new Device
def add_new_device(name: str, model: int, location: str):
    new_device = Device(
        name = name,
        id = model,
        location = location
	)
    session.add(new_device)
    try:
        session.commit()
        return True
    except Exception as e:
        # TODO: log error to 
        session.rollback()
        return False
    
# Update Device info
def update_device(model: int, updates: dict):
    device = session.query(Device).filter_by(id=model).first()
    for key, value in updates.items():
        if (hasattr(device, key)):
            setattr(device, key, value)
        else:
            raise KeyError
    try:
        session.commit()
        return device
    except Exception as e:
        # TODO: log error to file
        session.rollback()
        return False

# Get all devices
def get_all_devices():
    all_devices = session.query(Device).all()
    return all_devices

# Get specific device
def get_device(model: int):
    device = session.query(Device).filter_by(id=model).first()
    if device:
        return device
    return False

# Delete device
def delete_device(model: int):
    device = session.query(Device).filter_by(id=model).first()
    session.delete(device)
    try:
        session.commit()
        return True
    except Exception as e:
        # TODO: log error to file
        session.rollback()
        return False
