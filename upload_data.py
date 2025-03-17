from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
uri = "mongodb+srv://mayankapoor111:madhuK852774@cluster0.qvuql.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to server
client = MongoClient(uri)

# Create a database name and collection name
DATABASE_NAME = "sensor_db"
COLLECTION_NAME = 'waferfault'

df = pd.read_csv("C:\Users\Mayank kapoor\Desktop\sensorproject\notebooks\wafer_23012020_041211.csv")

df = df.drop("Unnamed: 0", axis=1)

json_record = list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)