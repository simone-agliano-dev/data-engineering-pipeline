from decouple import config
from pathlib import Path

# Data routing
DATA_FOLDER = "/app/data/"
BASE_DIR = Path(__file__).resolve(strict=True).parent
PATH_DIR = str(BASE_DIR) + DATA_FOLDER

# Data processing configuration
DATE = "2019-06-01"  # datetime.now().strftime("%Y-%m-%d")
ALLOWED_EXTENSIONS = {"json"}
N_BATCH_FILES = 50
JSON_CHUNKS_SIZE = 10000

# Access to Database
HOST = config("DB_ADDRESS")
PASSWORD = config("DB_PASS")
DB = config("DB_DATABASE")
USER = config("DB_USER")

# Fields Data Models
EVENT = ["event", "on", "at", "data", "organization_id"]
VEHICLES = ["id", "location"]
VEHICLES_DEREGISTER = ["id"]
OPERATING = ["id", "start", "finish"]
