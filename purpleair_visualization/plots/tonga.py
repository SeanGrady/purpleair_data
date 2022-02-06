import json
from purpleair_visualization.utils.get_sensor_data import (
    get_sensor_historical_data,
)
from purpleair.sensor import Sensor
import plotly.graph_objects as go
from purpleair_visualization.utils.get_sensor_data import SENSOR_METADATA_PATH
from datetime import date, datetime


CHANNEL = "child"
FIELD = "primary"
SENSOR_KEYS = (
    "sean",
    # "firestation",
    # "cherry_hill",
)
START_DATETIME = datetime(2022, 1, 15, 8, 0)
END_DATETIME = datetime(2022, 1, 15, 18, 0)
MAX_PRESSURE_MPA = 1028
MIN_PRESSURE_MPA = 1003


def plot_tonga_eruption():
    start_week = START_DATETIME.isocalendar().week
    current_week = date.today().isocalendar().week
    weeks_ago = (current_week - start_week)

    with open(SENSOR_METADATA_PATH, "r") as metadata:
        local_sensors = json.load(metadata)

    fig = go.Figure()

    for key in SENSOR_KEYS:
        # get sensor metadata and object
        sensor_metadata = local_sensors[key]
        sensor = Sensor(sensor_metadata["id"])

        # Load historical data
        print(f"Getting {weeks_ago} weeks of data for {key}")
        historical_data = get_sensor_historical_data(
            sensor=sensor,
            channel=CHANNEL,
            field=FIELD,
            weeks=weeks_ago + 1
        )
        historical_data.set_index("created_at", inplace=True)
        historical_data.sort_index(inplace=True)
        sliced_data = historical_data[START_DATETIME:END_DATETIME]
        # Create graph and add to figure
        sens_name = sensor.parent.name
        plot_label = sens_name if sens_name else sensor_metadata["display_name"]
        fig.add_trace(
            go.Scatter(
                x=sliced_data.index,
                y=sliced_data["Atmospheric Pressure"],
                mode="lines",
                name=plot_label,
            )
        )

    fig.update_xaxes(
        title_text="Date and Hour, UTC (mm-dd hh)",
    )
    fig.update_yaxes(
        # range=[MIN_PRESSURE_MPA, MAX_PRESSURE_MPA],
        title_text="Barometric Pressure (mbar)",
    )
    fig.update_layout(
        title="Barometric Pressure on 1/15/22, 8:00 to 18:00",
    )
    fig.show()
