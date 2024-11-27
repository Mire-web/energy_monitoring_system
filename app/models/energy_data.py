#!/usr/bin/python3
"""
Description: Defines model for energy data upload
"""
import datetime

# Define Energy Data Class

class Energy_Data():
    def __init__(self, did: int, voltage: float, current: float, power: float, ts: datetime):
        __device_id = did
        __voltage = voltage
        __current = current
        __power = power
        __timestamp = ts
        
    def voltage(self):
        return self.__voltage
    
    def current(self):
        return self.__current
    
    def power(self):
        return self.__power
    
    def timestamp(self):
        return self.__timestamp