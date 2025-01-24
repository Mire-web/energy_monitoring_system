#!/usr/bin/python3
"""
Description: Crud operations for device
"""
from app.crud import Session
from app.db.setup import Device


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
    if not device:
        add_new_device(updates['name'], model, updates['location'])
    else:
        for key, value in updates.items():
            if (hasattr(device, key)):
                setattr(device, key, value)
            else:
                return False
    try:
        session.commit()
        return {'success': True}
    except Exception as e:
        # TODO: log error to file
        print(e)
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
    if not device:
        return None
    session.delete(device)
    try:
        session.commit()
        return True
    except Exception as e:
        # TODO: log error to file
        session.rollback()
        return False
