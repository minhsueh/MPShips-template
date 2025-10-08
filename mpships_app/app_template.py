__description__ = "This app provides tools to visulize dielectric function."
__author__ = "cool_app_author"


from dash import Dash, html
from mp_api.client import MPRester
from dotenv import load_dotenv
import os

# Load MP_API_KEY from .env file
load_dotenv()
MP_API_KEY = os.getenv("MP_API_KEY")


def get_mpr():
    return MPRester(MP_API_KEY)


app = Dash(__name__, suppress_callback_exceptions=True, use_pages=False)

# add your design here
app.layout = html.Div()


# add your callback here
@app.callback()
def do_something():
    pass


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8051, debug=True)
