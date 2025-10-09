from core.utils import get_mpr
from dash import html, dcc

mpr = get_mpr()


def build_layout(app):
    return html.Div(
        [
            html.H2("Display dielectric function", style={"align": "center"}),
            html.Div(
                [
                    dcc.Input(id="input-box", value="Al-*", debounce=True),
                    html.Button("Enter", id="enter-btn", n_clicks=0),
                ]
            ),
            dcc.Loading(
                html.Div(
                    [
                        dcc.Graph(id="fig-real-dielec"),
                        dcc.Graph(id="fig-imag-dielec"),
                    ],
                    style={"display": "flex"},
                ),
            ),
        ]
    )
