import configparser
import pathlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from conf.models import Base

# Шлях до файлу конфігурації
file_config = pathlib.Path(__file__).parent.parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(file_config)

# Отримання параметрів підключення до бази даних з конфігурації
user = config.get('DEV_DB', 'USER')
password = config.get('DEV_DB', 'PASSWORD')
domain = config.get('DEV_DB', 'DOMAIN')
port = config.get('DEV_DB', 'PORT')
db = config.get('DEV_DB', 'DB_NAME')

# Створення URI для підключення до бази даних
URI = f"postgresql://{user}:{password}@{domain}:{port}/{db}"

# Створення двигуна бази даних
engine = create_engine(URI, echo=False, pool_size=5, max_overflow=0)

# Виклик методу create_all() для створення таблиць
Base.metadata.create_all(engine)

# Створення фабрики сесій
DBSession = sessionmaker(bind=engine)
session = DBSession()

