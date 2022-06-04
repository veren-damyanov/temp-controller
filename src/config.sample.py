"""
TODO: document

Device directory has a name like f'28-{device_id}'
Full path to the temperature file looks like:

f'{DEVICES_HOME}/28-{device_id}/temperature'

26123 -> 26.123 'C

"""

SENSORS_ROOT = '/sys/bus/w1/devices'

SENSORS = {
    'CPU1': '123',
    'CPU2': '456',
}

"""JSON

{
    "sensor-data": [
        {
            "sensor-id": "098237482703487234",
            "sensor-name": "CPU1",
            "raw-temp": 26123,
            "adjusted-temp": None,
        },
        {
            "sensor-id": "098237482703487234",
            "sensor-name": "CPU2",
            "raw-temp": 26123,
            "adjusted-temp": None,
        },
    ]
}

"""