## Quick start
#### Setup
Choose names: in this example, we’ll use the repo name `cool-app`.

```
# 1) Clone the template
git clone https://github.com/minhsueh/MPShips-template.git
mv MPShips-template cool-app
cd cool-app

# 2) Create & activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# 3) Install dependencies
pip install -r requirements.txt

# 4) Configure your Materials Project API key
echo 'MP_API_KEY=<YOUR_MP_API_KEY>' >> .env

# Optional (recommended for code quality)
pre-commit install # This will run basic checks (formatting, linting) before each commit.

```

Now start building your app code in the files under `mpships_app/user/` described below.


#### Local testing
```
python run.py # See your own design
python run.py --use_sample # See the sampled app
```

#### Where to put your code
Feel free to modify anything under `mpships_app/.` The main editable files are:`
 - `mpships_app/user/layout.py` — implement `build_layout(app)` to define the UI.
 - `mpships_app/user/callbacks.py` — implement `register_callbacks(app)` to wire callbacks.
 - `mpships_app/app_metadata.yaml` — fill in your app’s metadata.
 - Root `requirements.txt` — add any extra libraries your app needs.

The host loader will import `build_layout` and `register_callbacks` automatically.


#### Addidional notes

`get_mpr` is a light wrapper around the official [`mp_api`](https://api.materialsproject.org/)

Example:
```
from core.utils import get_mpr
mpr = get_mpr()

mpr.materials.summary.search(
            material_ids="mp-149",
            fields=["material_id", "has_props"]
        )
```
