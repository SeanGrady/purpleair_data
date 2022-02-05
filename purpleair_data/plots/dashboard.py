from


def plot_tonga_eruption():
    sean_sensor = Sensor(get_sensor_id_by_name("sean"))
    sean_data = get_sensor_historical_data(
        sean_sensor,
        "child",
        "primary",
        2,
    )
    ax = sean_data.plot(
        x="created_at",
        y="Atmospheric Pressure",
        label="Evergreen Estates",
    )

    cherry_hill_sensor = Sensor(get_sensor_id_by_name("sean"))
    cherry_hill_data = get_sensor_historical_data(
        cherry_hill_sensor,
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

    firestation_sensor = Sensor(get_sensor_id_by_name("sean"))
    firestation_data = get_sensor_historical_data(
        firestation_sensor,
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
