from enum import Enum
import os
from dotenv import load_dotenv

load_dotenv()


class AuthData(Enum):
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
