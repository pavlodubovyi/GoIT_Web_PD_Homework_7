import os
import pathlib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from conf.models import Base
from dotenv import load_dotenv

# Path to .env file
env_path = pathlib.Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# Getting database connection parameters from configuration
user = os.getenv('DB_USER')
password = os.getenv('DB_PASS')
db = os.getenv('DB_NAME')
domain = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')

# Creating URL for database connection
URI = f"postgresql://{user}:{password}@{domain}:{port}/{db}"

# Creating database engine
engine = create_engine(URI, echo=False, pool_size=5, max_overflow=0)

# Calling create_all() for creating tables
Base.metadata.create_all(engine)

# Creating session
DBSession = sessionmaker(bind=engine)
session = DBSession()

# print(URI)
