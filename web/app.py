import json
from flask import Flask, jsonify, request

from .database import session
from .database.tables import Sensor, Tool, Sensor_value
from datetime import datetime, timedelta
from sqlalchemy import func

app = Flask(__name__)


@app.route('/sensors/<int:sensor_id>/info', methods=['GET'])
def get_sensor_info(sensor_id):
    sensor=session.query(Sensor).get(sensor_id)
    return sensor.json()

@app.route('/node/tools', methods=['GET'])
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
def get_sensors():
    sensors = session.query(Sensor).all()
    return Sensor.json(sensors)

@app.route("/tools", methods=["GET"])
def get_tools():
    tools = session.query(Tool).all()
    return Tool.json(tools)

@app.route('/tools/<int:tool_id>/sensors', methods=['GET'])
def get_sensors_value_for_tool(tool_id):
    tool_sensors = session.query(Tool).get(tool_id).sensors
    tool_sensors_x_values = {}
    for item in tool_sensors:
        value = session.query(Sensor_value).filter(
        Sensor_value.sensor_id==item.sensor_id).order_by(Sensor_value.sensor_value_date.desc()).first()
        tool_sensors_x_values[item]= value
    tool_sensors_values = {}
    for tool in tool_sensors:
        for value in tool_sensors_x_values:
            if value.sensor_id == tool.sensor_id:
                tool_sensors_values[tool.sensor_name] = {
                "sensor_id":tool.sensor_id,
                "updated":tool_sensors_x_values[value].sensor_value_date,
                "value": tool_sensors_x_values[value].value}
    return jsonify(tool_sensors_values)


@app.route('/sensors/<int:sensor_id>', methods=['GET'])
def get_sensor_value_from_specific_time_range(sensor_id):
    time_range = request.args.get("time")
    if not time_range:
        time_range = 1
    end_time = datetime.now()
    begin_time = datetime.now() - timedelta(seconds=int(time_range))
    values = session.query(Sensor_value).filter(Sensor_value.sensor_value_date.between(begin_time,end_time))
    return Sensor_value.json(list(values))
    