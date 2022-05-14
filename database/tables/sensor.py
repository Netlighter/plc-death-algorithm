from database.connection import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from .sequences import sensor_table_sequence
from .tool import Tool


class Sensor(Base):
    __tablename__ = "SENSOR"

    sensor_id = Column(Integer, sensor_table_sequence, 
    server_default=sensor_table_sequence.next_value(), primary_key=True)

    sensor_name = Column(String, nullable=False)

    sensor_type = Column(String, nullable=False)

    tool_id = Column(Integer, ForeignKey(Tool.tool_id))

Tool.sensors = relationship("Sensor", uselist=True)
