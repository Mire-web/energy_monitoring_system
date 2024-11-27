#!/usr/bin/python3
"""
Main app script
"""
from crud.energy_data import *
from datetime import datetime, timedelta

def main():
    reading = get_aggregate_consumption()
    print('Voltage', '\tCurrent', '\tPower')
    if reading:
        print(reading['voltage'], '\t', reading['current'], '\t', reading['power'])
    else:
        print("Device not found")

if __name__=='__main__':
    main()
