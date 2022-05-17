import json
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from .database import session
from .database.tables import Sensor, Tool, Sensor_value
from datetime import datetime, timedelta
from sqlalchemy import func

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/sensors/<int:sensor_id>/info', methods=['GET'])
@cross_origin()
def get_sensor_info(sensor_id):
    sensor=session.query(Sensor).get(sensor_id)
    return sensor.json()

@app.route('/node/tools', methods=['GET'])
@cross_origin()
def get_tools_by_node():
    node = request.args.get("name")
    if node:
        node = node.lower()
    available_nodes = [node_name[0].lower() for node_name in session.query(Tool.node).distinct()]
    if node not in available_nodes:
        return f"Node with name '{node}' does not exist. Try {available_nodes}", 400
    tools = list(session.query(Tool).filter(func.lower(Tool.node) == node))
    return Tool.json(tools)
    
@app.route('/node/sensors', methods=['GET'])
@cross_origin()
def get_sensors_by_node():
    node = request.args.get("name")
    if node:
        node = node.lower()
    available_nodes = [node_name[0].lower() for node_name in session.query(Tool.node).distinct()]
    if node not in available_nodes:
        return f"Node with name '{node}' does not exist. Try {available_nodes}", 400
    sensors = session.query(Sensor, Tool).filter(Sensor.tool_id == Tool.tool_id).filter(func.lower(Tool.node) == node)
    result = {}
    for sensor in sensors:
        result[sensor[0].sensor_name] = {
            "sensor_id": sensor[0].sensor_id,
            "tool_id": sensor[1].tool_id,
            "tool_name": sensor[1].tool_name,
            "sensor_type": sensor[0].sensor_type
        }
    return json.dumps(result, ensure_ascii=False)

@app.route("/sensors", methods=["GET"])
@cross_origin()
def get_sensors():
    sensors = session.query(Sensor).all()
    return Sensor.json(sensors)

@app.route("/tools", methods=["GET"])
@cross_origin()
def get_tools():
    tools = session.query(Tool).all()
    return Tool.json(tools)

@app.route("/tool_values", methods=["GET"])
@cross_origin()
def get_tools_values():
    tools = []
    for tool in session.query(Tool).all():
        tools.append({
            "tool_id": tool.tool_id,
            "tool_name": tool.tool_name,
            "tool_state": tool.tool_state,
            "tool_accident": tool.tool_accident,
            "node": tool.node
        })
        tool_sensors = session.query(Tool).get(tool.tool_id).sensors
        tools[-1]["sensors"] = []
        for sensor in tool_sensors:
            sensor_values = session.query(Sensor_value).filter(Sensor_value.sensor_id == sensor.sensor_id).order_by(Sensor_value.sensor_value_date.desc()).first()
            tools[-1]["sensors"].append({
                "sensor_id": sensor.sensor_id,
                "sensor_name": sensor.sensor_name,
                "sensor_type": sensor.sensor_type,
                "updated": str(sensor_values.sensor_value_date),
                "value": sensor_values.value
            })

    return json.dumps(tools, ensure_ascii=False)

@app.route('/tools/<int:tool_id>/sensors', methods=['GET'])
@cross_origin()
def get_sensors_value_for_tool(tool_id):
    tool_sensors = session.query(Tool).get(tool_id).sensors
    tool_sensors_x_values = {}
    for item in tool_sensors:
        value = session.query(Sensor_value).filter(
        Sensor_value.sensor_id==item.sensor_id).order_by(Sensor_value.sensor_value_date.desc()).first()
        tool_sensors_x_values[item]= value
    tool_sensors_values = {}
    print(tool_sensors_x_values)
    for tool in tool_sensors:
        for value in tool_sensors_x_values:
            if value.sensor_id == tool.sensor_id:
                tool_sensors_values["sensor"] = {
                "sensor_name": tool.sensor_name,
                "sensor_id":tool.sensor_id,
                "updated":tool_sensors_x_values[value].sensor_value_date,
                "value": tool_sensors_x_values[value].value}
    return jsonify(tool_sensors_values)


@app.route('/sensors/<int:sensor_id>', methods=['GET'])
@cross_origin()
def get_sensor_value_from_specific_time_range(sensor_id):
    time_range = request.args.get("time")
    sensor_values = session.query(Sensor_value).filter(Sensor_value.sensor_id == sensor_id).order_by(Sensor_value.sensor_value_date.desc())
    if not time_range:
        sensor_values = sensor_values.all()
        if not sensor_values:
            sensor_values = []
    else:
        end_time = datetime.now()
        begin_time = datetime.now() - timedelta(seconds=int(time_range))
        sensor_values = sensor_values.filter(Sensor_value.sensor_value_date.between(begin_time,end_time))
    return Sensor_value.json(list(sensor_values))
    