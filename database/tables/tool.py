from database.connection import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from .sequences import tool_table_sequence


class Tool(Base):
    __tablename__ = "TOOL"

    tool_id = Column(Integer, tool_table_sequence, 
    server_default=tool_table_sequence.next_value(), primary_key=True)

    tool_name = Column(String, nullable=False)

    tool_state = Column(String, nullable=False)

    tool_accident = Column(Boolean, nullable=False)
