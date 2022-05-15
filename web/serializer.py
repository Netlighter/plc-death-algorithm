import json
from datetime import datetime
from sqlalchemy.sql.sqltypes import DateTime


def obj_to_dict(inst, cls):
    convert = dict()
    d = dict()
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        for type in convert:         
            if isinstance(c.type, type) and v is not None:
                try: 
                    d[c.name] = convert[type](v)  
                except:
                    d[c.name] = "Error:  Failed to covert using ", str(convert[type])
        if v is None:
            d[c.name] = str()
        else:
            d[c.name] = v
    return d

def to_json(inst, cls):
    if isinstance(inst, list):
        result = []
        for obj in inst:
            result.append(obj_to_dict(obj, cls))
    else:
        result = obj_to_dict(inst, cls)
    return json.dumps(result, ensure_ascii=False,default=str)
