from .. import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, String, DateTime
from sqlalchemy.orm import relationship
from .sensor import Sensor
from .sequences import sensor_value_table_sequence
from web import to_json


class Sensor_value(Base):
    __tablename__ = "SENSOR_VALUE"

    sensor_id = Column(Integer, ForeignKey(Sensor.sensor_id), primary_key=True)

    sensor_value_date = Column(DateTime, primary_key=True)

    value = Column(String, nullable=False)

    @property
    def json(self):
        return to_json(self, self.__class__)

Sensor.values = relationship("Sensor_value", uselist=True)