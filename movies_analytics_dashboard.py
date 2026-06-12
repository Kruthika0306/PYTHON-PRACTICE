import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def main():

    movies = pd.DataFrame({
        "Movie": [
            "Movie A",
            "Movie B",
            "Movie C",
            "Movie D",
            "Movie E"
        ],
        "Rating": [8.5, 7.8, 9.1, 8.0, 7.5],
        "Revenue": [120, 95, 180, 130, 85],
        "Genre": [
            "Action",
            "Drama",
            "Action",
            "Comedy",
            "Drama"
        ]
    })

    genre_counts = movies["Genre"].value_counts()

    fig = make_subplots(
        rows=2,
        cols=2,
        specs=[
            [{"type": "bar"}, {"type": "pie"}],
            [{"type": "scatter"}, {"type": "bar"}]
        ],
        subplot_titles=(
            "Movie Ratings",
            "Genre Distribution",
            "Rating vs Revenue",
            "Revenue by Movie"
        )
    )

    # Ratings
    fig.add_trace(
        go.Bar(
            x=movies["Movie"],
            y=movies["Rating"],
            name="Ratings"
        ),
        row=1,
        col=1
    )

    # Genre Pie Chart
    fig.add_trace(
        go.Pie(
            labels=genre_counts.index,
            values=genre_counts.values
        ),
        row=1,
        col=2
    )

    # Scatter Plot
    fig.add_trace(
        go.Scatter(
            x=movies["Rating"],
            y=movies["Revenue"],
            mode="markers+text",
            text=movies["Movie"],
            textposition="top center"
        ),
        row=2,
        col=1
    )

    # Revenue Chart
    fig.add_trace(
        go.Bar(
            x=movies["Movie"],
            y=movies["Revenue"]
        ),
        row=2,
        col=2
    )

    fig.update_layout(
        title="Movie Analytics Dashboard",
        height=800,
        width=1200,
        template="plotly_dark"
    )

    fig.show()


if __name__ == "__main__":
    main()
