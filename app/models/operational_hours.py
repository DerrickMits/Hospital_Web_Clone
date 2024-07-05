#!/usr/bin/python3
""" holds class OperationHours """
import hospital_models as models
from hospital_models.base_model import HospitalBaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class OperationHours(HospitalBaseModel, Base):
    """Representation of Operation Hours """
    if models.storage_t == 'db':
        __tablename__ = 'operation_hours'
        facility_id = Column(String(60), ForeignKey('facilities.id'), nullable=False)
        day_of_week = Column(String(20), nullable=False)
        opening_time = Column(String(5), nullable=False)  # Format: HH:MM
        closing_time = Column(String(5), nullable=False)  # Format: HH:MM
        facility = relationship("Facility", backref="operation_hours")
    else:
        facility_id = ""
        day_of_week = ""
        opening_time = ""
        closing_time = ""

    def __init__(self, *args, **kwargs):
        """initializes Operation Hours"""
        super().__init__(*args, **kwargs)
