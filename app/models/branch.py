#!/usr/bin/python3
""" holds class Branch """
import hospital_models as models
from hospital_models.base_model import HospitalBaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class Branch(HospitalBaseModel, Base):
    """Representation of Branch """
    if models.storage_t == 'db':
        __tablename__ = 'branches'
        name = Column(String(128), nullable=False)
        address = Column(String(256), nullable=False)
        contact_number = Column(String(20), nullable=False)
        city = Column(String(60), nullable=False)
        services = relationship("Service", backref="branch")
    else:
        name = ""
        address = ""
        contact_number = ""
        city = ""

    def __init__(self, *args, **kwargs):
        """initializes Branch"""
        super().__init__(*args, **kwargs)
