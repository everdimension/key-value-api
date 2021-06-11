import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

database_url = os.environ.get('DB_URL')
username = os.environ.get('DB_USERNAME')
password = os.environ.get('DB_PASSWORD')

client = MongoClient(f'mongodb+srv://{username}:{password}@{database_url}')

db = client.testingtesting

