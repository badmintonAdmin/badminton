import os
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG_MODE = os.getenv("DEBUG") == "True"

print(f"Подключение к БД: {DATABASE_URL}")
print(f"Режим отладки: {DEBUG_MODE}")
