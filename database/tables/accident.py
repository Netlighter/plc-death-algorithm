from database.connection import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from .accident_type import Accident_type


class Accident(Base):
    __tablename__ = "ACCIDENT"

    accident_type_id = Column(Integer, ForeignKey("Accident_type.accident_type_id"), primary_key=True)

    data = Column(String, primary_key=True)

    accident_name = Column(String, nullable=False)
    accident_status = Column(String, nullable=False)
    accident_logs = Column(String, nullable=False)

