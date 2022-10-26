import os
import environ
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(env_file=os.path.join(BASE_DIR, '.env'))

API_TOKEN = env('TELEGRAM_API_TOKEN')
ACCESS_ID = env('TELEGRAM_ACCESS_ID')
TIMEZONE = str(env("TIMEZONE"))
