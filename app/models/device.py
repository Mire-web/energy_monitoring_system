#!/usr/bin/python3
"""
Description: Defines model for devices
"""
import datetime

# Define Device Class
class Device():
    def __init__(self, name: str, location: str):
        __name = name
        __location = location
        __created_at = datetime.datetime.now()
        
    def dname(self):
        return self.__name
    
    def dname(self, name: str):
        self.__name = name

    def location(self):
        return self.__location
    
    def location(self, location: str):
        self.__location = location
        
    def created_at(self):
        return self.__created_at