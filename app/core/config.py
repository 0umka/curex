from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.environ['SECRET_KEY']
ALGORITHM = os.environ['ALGORITHM']
CURRENT_TIME = datetime.now()
EXPIRATION_TIME = timedelta(minutes=15)
