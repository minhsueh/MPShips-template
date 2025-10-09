import sys
import importlib
from dash import Dash, html
from pathlib import Path


def create_app() -> Dash:
    app = Dash(__name__, suppress_callback_exceptions=True, use_pages=False)

    try:
        parent = (Path(__file__).parent.parent).resolve()
        if str(parent) not in sys.path:
            sys.path.insert(0, str(parent))

        layout_mod = importlib.import_module("user.layout")
        callbacks_mod = importlib.import_module("user.callbacks")
    except ModuleNotFoundError:
        app.layout = html.Div("Add your layout in user/layout.py")
        return app

    # Users implement these two functions:
    app.layout = layout_mod.build_layout(app)
    callbacks_mod.register_callbacks(app)

    return app
