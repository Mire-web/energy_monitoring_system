#!/usr/bin/python3
"""
Description: Set up database engine for Device storage and energy monitoring
"""
from datetime import datetime
from sqlalchemy import create_engine, Column, String, ForeignKey, Integer, Float, DateTime
from sqlalchemy.orm import relationship, declarative_base

engine = create_engine("sqlite:///database/energy_consumption.db", echo=False)
Base = declarative_base()

class Device(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    energy_consumption = relationship('Energy_data', back_populates='device')
    
class Energy_data(Base):
    __tablename__ = "energy_consumption"
    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(Integer, ForeignKey("devices.id"))
    device = relationship("Device", back_populates="energy_consumption")
    voltage = Column(Float, nullable=False)
    current = Column(Float, nullable=False)
    power = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    
    def as_dict(self):
        return {
            "id": self.id,
			"device": self.device.name,
            "device-model": self.device_id,
            "voltage": self.voltage,
            "current": self.current,
            "power": self.power,
            "timestamp": self.timestamp
		}

Base.metadata.create_all(engine)
