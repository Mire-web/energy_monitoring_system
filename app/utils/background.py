#!/usr/bin/python3
"""
Background Process to monitor energy in real time
"""
from app.crud import Session
from app.crud.alert import Alert_history, Alert_threshold
from app.schemas.schema import EnergyDataSchema
from app.crud.alert import add_alert_to_history
from sqlalchemy import and_

session = Session()

def send_email_notification():
    pass

def web_notification():
    pass

def check_data_against_threshold(new_data: EnergyDataSchema):
    # query db for threshold
    device_current = session.query(Alert_threshold).filter(and_(Alert_threshold.device_id == new_data.did, Alert_threshold.parameter == "current")).first()
    device_voltage = session.query(Alert_threshold).filter(and_(Alert_threshold.device_id == new_data.did, Alert_threshold.parameter == "voltage")).first()
    # compare threshold to new data
    if new_data.voltage > device_voltage.threshold_value:
        # trigger alert
        print("Voltage Threshold Exceeded")
        # web_notification(new_data)
        # send_email_notification(new_data)
        # log alert to db
        add_alert_to_history(new_data.did, "voltage", new_data.voltage)

    if new_data.current > device_current.threshold_value:
        # trigger alert
        print("Current Threshold Exceeded")
        # web_notification(new_data)
        # send_email_notification(new_data)
        # log alert to db
        add_alert_to_history(new_data.did, "current", new_data.current)
