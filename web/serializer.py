import json
from datetime import datetime


def to_json(inst, cls):
    
    convert = dict()
    d = dict()
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        if c.type in convert.keys() and v is not None:
            try:
                d[c.name] = convert[c.type](v)
                
            except:
                d[c.name] = "Error:  Failed to covert using ", str(convert[c.type])
        if c.type  in convert.keys() and c.type is datetime:
            print('yes')
            d[c.name] = convert[str](v)
        elif v is None:
            d[c.name] = str()
        else:
            d[c.name] = v
    if type(d) is not datetime:
        return json.dumps(d, ensure_ascii=False)
    else:
        return json.dumps(str(d), ensure_ascii=False)