from database.connection import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from .sensor import Sensor


class Sensor_value(Base):
    __tablename__ = "SENSOR_VALUE"

    sensor_id = Column(Integer, ForeignKey("Sensor.sensor_id"), primary_key=True)

    sensor_value_date = Column(String, primary_key=True)

    value = Column(String, nullable=False)

Sensor.value = relationship("Sensor_value", uselist=True)