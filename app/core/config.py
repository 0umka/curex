import secrets
from datetime import datetime, timedelta


SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS256"
CURRENT_TIME = datetime.now()
EXPIRATION_TIME = timedelta(minutes=15)
