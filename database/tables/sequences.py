from sqlalchemy import MetaData, Sequence

meta = MetaData()

tool_table_sequence = Sequence('tool_id_seq', metadata=meta)
sensor_table_sequence = Sequence('sensor_id_seq', metadata=meta)
accident_type_table_sequence = Sequence('accident_type_id_seq', metadata=meta)
