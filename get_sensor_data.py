import json
from pprint import pprint
from purpleair.sensor import Sensor


TEST_SENSOR_NAME = "sean_home_outdoor"


def get_sensor_id(sensor_name):
    with open("/home/sgrady/dev/purpleair_data/sensor_metadata.json", "r") as metadata:
        sensor_metadata = json.load(metadata)
        sensor_id = sensor_metadata[sensor_name]["id"]
    return sensor_id


def get_sensor_historical_data(sensor_name):
    sensor_id = get_sensor_id(sensor_name)
    sensor = Sensor(sensor_id)
    primary_channel = sensor.parent
    historical_dataframe = primary_channel.get_historical(
        weeks_to_get=1,
        thingspeak_field="primary",
    )
    return historical_dataframe


if __name__ == "__main__":
    pprint(get_sensor_historical_data(TEST_SENSOR_NAME).head)
