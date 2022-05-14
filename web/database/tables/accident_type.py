from .. import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from .sequences import accident_type_table_sequence
from .tool import Tool
from web import to_json


class Accident_type(Base):
    __tablename__ = "ACCIDENT_TYPE"

    accident_type_id = Column(Integer, accident_type_table_sequence,
    server_default=accident_type_table_sequence.next_value(), primary_key=True)

    accident_type = Column(String, nullable=False)

    tool_id = Column(Integer, ForeignKey(Tool.tool_id))

    @property
    def json(self):
        return to_json(self, self.__class__)

Tool.accident_types = relationship("Accident_type", uselist=True)
