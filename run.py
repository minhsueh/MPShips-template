from core.factory import create_app
from core.host_config import host_settings

app = create_app()

if __name__ == "__main__":
    app.run_server(
        host=host_settings.HOST, port=host_settings.PORT, debug=host_settings.DEBUG
    )
