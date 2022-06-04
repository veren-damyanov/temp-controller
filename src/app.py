import asyncio
import json
from os import path

from sanic import Sanic
from sanic import response

from config import SENSORS, SENSORS_ROOT


app = Sanic("MyHelloWorldApp")


async def read_temp(sensor_name):
    sensor_id = SENSORS.get(sensor_name)
    data = {'sensor-id': sensor_id, 'sensor-name': sensor_name, 'raw-temp': None, 'adjusted-temp': None}
    with open(path.join(SENSORS_ROOT, sensor_id, 'temperature')) as flh:
        data['raw-temp'] = int(flh.read().strip())
    return data


@app.get("/temperature")
async def get_temperature(request):
    final_data = {'sensor_data': []}
    results = await asyncio.gather(*(read_temp(sensor_id) for sensor_id in SENSORS.keys()))
    for result in results:
        final_data['sensor_data'].append(result)
    return response.json(final_data)
