#!/usr/bin/python3
"""
Define Schemas for query parameters
for Device and Energy_data
"""
from pydantic import BaseModel, StringConstraints
from typing_extensions import Annotated
from datetime import datetime

class DeviceCreateSchema(BaseModel):
    id: int
    name: Annotated[str, StringConstraints(
		strip_whitespace=True, min_length=1
	)]
    location: Annotated[str, StringConstraints(
		strip_whitespace=True, min_length=1
	)]

class UpdateDeviceCreateSchema(BaseModel):
    id: int
    name: Annotated[str, StringConstraints(
		strip_whitespace=True
	)] | None = None
    location: Annotated[str, StringConstraints(
		strip_whitespace=True
	)] | None = None


class EnergyDataSchema(BaseModel):
    did: int
    voltage: float
    current: float

class Date(BaseModel):
    date: datetime
