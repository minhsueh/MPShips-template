__description__ = "This app show some cool stuff."
__author__ = "cool_app_author"


from dash import Dash, html, dcc, callback, Output, Input, MATCH, State, ctx

class CoolAPP(html.Div):
    


if __name__ == "__main__":
    app = Dash(__name__, suppress_callback_exceptions=True, use_pages=False)
    app.run_server(host='0.0.0.0', port=8051, debug=True)