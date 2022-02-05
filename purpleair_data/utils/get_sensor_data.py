import json
from pprint import pprint
from purpleair.sensor import Sensor
from datetime import datetime
import pandas


SENSOR_METADATA_PATH = "/home/sgrady/dev/sensor_data/sensor_metadata.json"


def get_sensor_id_by_name(sensor_name: str):
    with open(SENSOR_METADATA_PATH, "r") as metadata:
        sensor_metadata = json.load(metadata)
        sensor_id = sensor_metadata[sensor_name]["id"]
    return sensor_id


def get_sensor_historical_data(
    sensor: Sensor,
    channel: str,
    field: str,
    weeks: int,
) -> pandas.DataFrame:
    channels = {
        "parent": sensor.parent,
        "child": sensor.child,
    }
    historical_dataframe = channels[channel].get_historical(
        weeks_to_get=weeks,
        thingspeak_field=field,
    )
    return historical_dataframe
