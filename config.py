import os

DB_CONNECTION_URI = os.environ.get("DB_CONNECTION_URI")
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = int(os.environ.get("DB_PORT", "27017"))
DB_NAME = os.environ.get("DB_NAME", "doc_db_loadtest")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_USE_SSL = os.environ.get("DB_USE_SSL", 'False').lower() in ['true', '1']

N_THREADS = int(os.environ.get("N_THREADS", 100))
DURATION = int(os.environ.get("DURATION", 20))

S3_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME")
SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")
