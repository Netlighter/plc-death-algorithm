from database.connection import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, String
from sqlalchemy.orm import relationship
from .sensor import Sensor
from .sequences import sensor_value_table_sequence


class Sensor_value(Base):
    __tablename__ = "SENSOR_VALUE"

    # sensor_value_id = Column(Integer, sensor_value_table_sequence, server_default=sensor_value_table_sequence.next_value(), primary_key=True)

    sensor_id = Column(Integer, ForeignKey(Sensor.sensor_id), primary_key=True)

    sensor_value_date = Column(String, primary_key=True)

    value = Column(String, nullable=False)

Sensor.value = relationship("Sensor_value", uselist=True)