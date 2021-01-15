import os

DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = int(os.environ.get("DB_PORT", "27017"))
DB_NAME = os.environ.get("DB_NAME", "doc_db_loadtest")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

N_THREADS = int(os.environ.get("N_THREADS", 100))
DURATION = int(os.environ.get("DURATION", 60))
