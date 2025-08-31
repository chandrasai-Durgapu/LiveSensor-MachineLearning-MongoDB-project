
import sys
from typing import Optional

import numpy as np
import pandas as pd
import json
from sensor.configuration.mongodb_connection import MongoDBClient
from sensor.constant.database import DATABASE_NAME
from sensor.exception import SensorException
import time
from sensor.logger import logging

class SensorData:
    """
    This class help to export entire mongo db record as pandas dataframe
    """

    def __init__(self):
   
        try:

            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
            # Step 1: Connect to MongoDB
            step_start = time.perf_counter()
            # your MongoDB connection code
            logging.info(f"MongoDB client database {time.perf_counter() - step_start:.2f} seconds")

        except Exception as e:
            raise SensorException(e, sys)


    def save_csv_file(self,file_path ,collection_name: str, database_name: Optional[str] = None):
        try:
            # Step 3: Convert to DataFrame
            step_start = time.perf_counter()
                # read csv file path
            data_frame=pd.read_csv(file_path)
            logging.info(f"Read csv file and store in DataFrame{time.perf_counter() - step_start:.2f} seconds")
            
            data_frame.reset_index(drop=True, inplace=True)
            records = list(json.loads(data_frame.T.to_json()).values())
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
                
            step_start = time.perf_counter()
                # insert records MongoDB Atlas
            collection.insert_many(records)
            logging.info(f"Collection records insert in MongoDB Atlas{time.perf_counter() - step_start:.2f} seconds")
            
            logging.info("length of total records inserted{len(records)}")
            return len(records)
        except Exception as e:
            raise SensorException(e, sys)


    def export_collection_as_dataframe(
        self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        try:
            """
            export entire collectin as dataframe:
            return pd.DataFrame of collection
            """
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
                step_start = time.perf_counter()
            df = pd.DataFrame(list(collection.find()))
            logging.info(f"MongoDB Atlas records converted as DataFrame{time.perf_counter() - step_start:.2f} seconds")
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)

            df.replace({"na": np.nan}, inplace=True)
            

            return df

        except Exception as e:
            raise SensorException(e, sys)
