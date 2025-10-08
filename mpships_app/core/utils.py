from mp_api.client import MPRester
from dotenv import load_dotenv
import os

# Load MP_API_KEY from .env file
load_dotenv()
MP_API_KEY = os.getenv("MP_API_KEY")


def get_mpr():
    return MPRester(MP_API_KEY)
