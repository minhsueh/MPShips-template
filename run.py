from mpships_app.core.factory import create_app
from mpships_app.core.host_config import host_settings
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--use_sample", action="store_true", help="Enable sample mode (boolean flag)."
    )

    args = parser.parse_args()
    use_sample = args.use_sample

    app = create_app(use_sample=use_sample)

    app.run_server(
        host=host_settings.HOST, port=host_settings.PORT, debug=host_settings.DEBUG
    )
