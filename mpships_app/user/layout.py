from core.utils import get_mpr
from dash import html

mpr = get_mpr()


def build_layout(app):
    return html.Div(
        html.H2(["Your cool design should be here!"]), style={"textAlign": "center"}
    )
