import json
from pprint import pprint
from purpleair.sensor import Sensor
from datetime import datetime
from matplotlib import pyplot as plt
import pandas



def get_sensor_id(sensor_name):
    with open("/home/sgrady/dev/purpleair_data/sensor_metadata.json", "r") as metadata:
        sensor_metadata = json.load(metadata)
        sensor_id = sensor_metadata[sensor_name]["id"]
    return sensor_id


def get_sensor_historical_data(
    sensor_name: str,
    channel: str,
    field: str,
    weeks: int,
) -> pandas.DataFrame:
    sensor_id = get_sensor_id(sensor_name)
    sensor = Sensor(sensor_id)
    channels = {
        "parent": sensor.parent,
        "child": sensor.child,
    }
    historical_dataframe = channels[channel].get_historical(
        weeks_to_get=weeks,
        thingspeak_field=field,
    )
    return historical_dataframe


def plot_pressure_daata(
    sensor_name: str,
):
    sensor_data = get_sensor_historical_data(sensor_name)
    sensor_data.plot()


def plot_tonga_eruption():
    sean_data = get_sensor_historical_data(
        "sean",
        "child",
        "primary",
        2,
    )
    ax = sean_data.plot(
        x="created_at",
        y="Atmospheric Pressure",
        label="Evergreen Estates",
    )

    cherry_hill_data = get_sensor_historical_data(
        "cherry_hill",
        "child",
        "primary",
        2,
    )
    cherry_hill_data.plot(
        x="created_at",
        y="Atmospheric Pressure",
        ax=ax,
        label="Cherry Hill",
    )

    firestation_data = get_sensor_historical_data(
        "firestation",
        "child",
        "primary",
        2,
    )
    firestation_data.plot(
        x="created_at",
        y="Atmospheric Pressure",
        ax=ax,
        label="Firestation (or maybe Safeway)",
    )

    start_datetime = datetime(2022, 1, 15, 8, 0)
    end_datetime = datetime(2022, 1, 15, 18, 0)
    plt.xlim(start_datetime, end_datetime)
    plt.ylim(1003, 1028)

    plt.title("Barometric Pressure on 1/15/22, 8:00 to 18:00")
    plt.xlabel("Date and Hour, UTC (mm-dd hh)")
    plt.ylabel("Barometric Pressure (mbar)")

    plt.legend(bbox_to_anchor=(1.03, 0.5), loc="center left")
    plt.savefig("WHOA.png", bbox_inches="tight")

    plt.show()


if __name__ == "__main__":
    plot_tonga_eruption()
