import sys
import importlib
from dash import Dash, html
from pathlib import Path


def create_app(use_sample: bool = False) -> Dash:
    app = Dash(__name__, suppress_callback_exceptions=True, use_pages=False)

    try:
        parent = (Path(__file__).parent.parent).resolve()
        if str(parent) not in sys.path:
            sys.path.insert(0, str(parent))

        if not use_sample:
            layout_path = "user.layout"
            callbacks_path = "user.callbacks"
        else:
            layout_path = "user_sample.layout"
            callbacks_path = "user_sample.callbacks"

        layout_mod = importlib.import_module(layout_path)
        callbacks_mod = importlib.import_module(callbacks_path)
    except ModuleNotFoundError:
        app.layout = html.Div("Add your layout in user/layout.py")
        return app

    # Users implement these two functions:
    app.layout = layout_mod.build_layout(app)
    callbacks_mod.register_callbacks(app)

    return app
