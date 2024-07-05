#!/usr/bin/python3
""" holds class Service """
import hospital_models as models
from hospital_models.base_model import HospitalBaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum

class ServiceType(enum.Enum):
    IN_PATIENT = "in-patient"
    OUT_PATIENT = "out-patient"

class Service(HospitalBaseModel, Base):
    """Representation of Service """
    if models.storage_t == 'db':
        __tablename__ = 'services'
        facility_id = Column(String(60), ForeignKey('facilities.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        price = Column(Integer, nullable=False, default=0)
        service_type = Column(Enum(ServiceType), nullable=False)
        facility = relationship("Facility", backref="services")
    else:
        facility_id = ""
        name = ""
        description = ""
        price = 0
        service_type = ""

    def __init__(self, *args, **kwargs):
        """initializes Service"""
        super().__init__(*args, **kwargs)
