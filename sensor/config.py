from dataclasses import dataclass
import os
import pymongo


import warnings
from cryptography.utils import CryptographyDeprecationWarning

@dataclass

class EnvironmentVariable:
      mongo_db_url:str = os.getenv("MONGO_DB_URL")


# Use a context manager to temporarily suppress the cryptography warning.
# This is a short-term workaround.
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)


env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
print("MongoDB client initialized successfully.")

# Example: Get server info to test the connection.
try:
    print(mongo_client.server_info())
except Exception as e:
    print(f"Connection failed: {e}")
from dataclasses import dataclass
import os
import pymongo

@dataclass


class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")



env_var = EnvironmentVariable()

mongo_client = pymongo.MongoClient(env_var.mongo_db_url)