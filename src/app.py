import asyncio
from os import path

import aiofiles
from sanic import Sanic
from sanic import response

from config import SENSORS, SENSORS_ROOT


app = Sanic('temp-controller')


async def read_temp(sensor_name):
    sensor_id = SENSORS[sensor_name]
    async with aiofiles.open(path.join(SENSORS_ROOT, sensor_id, 'temperature')) as fhl:
        raw_temp = int((await fhl.read()).strip())
    return {
        'sensor-id': sensor_id,
        'sensor-name': sensor_name,
        'raw-temp': raw_temp,
        'adjusted-temp': None,
    }


@app.get('/temperature')
async def get_temperature(request):
    sensor_data = await asyncio.gather(*(read_temp(sensor_id) for sensor_id in SENSORS.keys()))
    return response.json({'sensor-data': sensor_data})
