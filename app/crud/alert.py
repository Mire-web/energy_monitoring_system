#!/usr/bin/python3
"""
Description: Crud operations for Alerts triggers and history
"""
from app.crud import Session
from datetime import datetime
from app.db.setup import Energy_data
from app.db.setup import Device
from app.db.setup import Alert_history
from app.db.setup import Alert_threshold
from sqlalchemy import func, and_


session = Session()


# Add new alert threshold
def add_limit(did: int, param: str, threshold: float):
    device = session.query(Device).filter(Device.id == did).first()
    thres = session.query(Alert_threshold).filter(and_(Alert_threshold.device_id == did, Alert_threshold.parameter == param)).first()
    if not device:
        raise ValueError("Device not found")
    if thres:
        raise ValueError("Parameter Already exists, Use the Update function")
    new_threshold = Alert_threshold(
        device_id = device.id,
        parameter = param,
        threshold_value = threshold
	)
    session.add(new_threshold)
    try:
        session.commit()
        return True
    except Exception as e:
        # TODO: log error to file
        session.rollback()
        return False
    
# Get device thresholds (optional parameter [value])
def get_device_limit(did: int, value: str | None):
    device = session.query(Device).filter(Device.id == did).first()
    if not device:
        return None
    if not value:
        return device.alert_threshold
    elif value:
        threshold = session.query(Alert_threshold).filter(Alert_threshold.parameter == value).join(Device, Alert_threshold.device_id == Device.id).order_by(Alert_threshold.id).all()
        threshold = [value.as_dict() for value in threshold]
        if threshold:
            return threshold
        return None

# Get all alert thresholds
def get_alert_thresholds():
    alerts = session.query(Alert_threshold).order_by(Alert_threshold.id).all()
    if not alerts:
        return None
    return alerts
    
# Update device threshold
def update_device_limit(did: int, parameter: str, value: float):
    threshold = session.query(Alert_threshold).filter(and_(Alert_threshold.device_id == did, Alert_threshold.parameter == parameter)).first()
    if not threshold:
        return f"No threshold set on device-{did} for {parameter}"
    try:
        threshold.threshold_value = value
        threshold.updated_at = datetime.now()
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        return e

# Add new alert history
def add_alert_to_history(did: int, parameter: str, trigger_value: float):
    device = session.query(Device).filter(Device.id == did).first()
    thres = session.query(Alert_threshold).filter(Alert_threshold.parameter == parameter).first()
    if not device:
        raise ValueError("Device not found")
    if not thres:
        raise ValueError("Alert threshold not found")
    new_alert = Alert_history(
        device_id = did,
        parameter = parameter,
        threshold = thres.threshold_value,
        trigger_value = trigger_value
        )
    try:
        session.add(new_alert)
        session.commit()
        return True
    except Exception as e:
        print(e)
        session.rollback()
        return str(e)
    
#Get alert history
def get_alerts():
    alerts = session.query(Alert_history).order_by(Alert_history.id).all()
    if alerts:
        return alerts
    return None

# Get Alert history for device (optional parameter [value, startDate, endDate])
def get_device_alert_history(did: int, parameter: str | None, startDate: datetime | None, endDate: datetime | None):
    device = session.query(Device).filter(Device.id == did).first()
    if not device:
        raise ValueError("Device not found")
    alerts = session.query(Alert_history).filter(Alert_history.device_id == did)
    if parameter:
        alerts = alerts.filter(Alert_history.parameter == parameter)
    if startDate:
        alerts = alerts.filter(func.date(Alert_history.created_at) >= startDate.date())
    if endDate:
        alerts = alerts.filter(func.date(Alert_history.created_at) <= endDate.date())
        
    alerts = alerts.order_by(Alert_history.id).all()
    alert_history = [alert.as_dict() for alert in alerts]
    return alert_history
