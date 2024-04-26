from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = "123"#os.environ['SECRET_KEY']
ALGORITHM = "123"#os.environ['ALGORITHM']
CURRENT_TIME = datetime.now()
EXPIRATION_TIME = timedelta(minutes=15)
