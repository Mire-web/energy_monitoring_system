#!/usr/bin/python3
"""
Script for populating the database with dummy data
"""
import csv
from app.crud import Session
from app.db.setup import Energy_data
from datetime import datetime


session = Session()

def populate_db():
    # read csv file
    with open('../energy_monitoring_dataset.csv', 'r') as data:
        dataset = csv.reader(data)
        next(dataset)
        for row in dataset:
            new_energy_data = Energy_data(
                device_id = row[0],
                voltage = row[2],
                current = row[3],
                power = row[4],
                timestamp = datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S')
                )
            # insert each row into db
            session.add(new_energy_data)
    # commit session to db
    try:
        session.commit()
        print('Operation Successful')
        return True
    except Exception as e:
        print(e)
        session.rollback()
        return False
    # close cursor
    finally:
        session.close()
