import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def main():

    weather_data = pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "Temperature": [30, 32, 31, 29, 28, 30, 33],
        "Humidity": [75, 70, 72, 80, 85, 78, 73],
        "WindSpeed": [12, 15, 10, 8, 11, 14, 16],
        "Rainfall": [5, 10, 2, 15, 20, 8, 3]
    })

    fig = make_subplots(
        rows=2,
        cols=2,
        subplot_titles=(
            "Temperature Trend",
            "Humidity Trend",
            "Wind Speed",
            "Rainfall"
        )
    )

    # Temperature
    fig.add_trace(
        go.Scatter(
            x=weather_data["Day"],
            y=weather_data["Temperature"],
            mode="lines+markers",
            name="Temperature"
        ),
        row=1,
        col=1
    )

    # Humidity
    fig.add_trace(
        go.Bar(
            x=weather_data["Day"],
            y=weather_data["Humidity"],
            name="Humidity"
        ),
        row=1,
        col=2
    )

    # Wind Speed
    fig.add_trace(
        go.Scatter(
            x=weather_data["Day"],
            y=weather_data["WindSpeed"],
            mode="lines+markers",
            name="Wind Speed"
        ),
        row=2,
        col=1
    )

    # Rainfall
    fig.add_trace(
        go.Bar(
            x=weather_data["Day"],
            y=weather_data["Rainfall"],
            name="Rainfall"
        ),
        row=2,
        col=2
    )

    fig.update_layout(
        title="Weekly Weather Dashboard",
        height=800,
        width=1200,
        template="plotly_dark"
    )

    fig.show()


if __name__ == "__main__":
    main()
