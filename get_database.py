from pymongo import MongoClient

def get_database():
    # MongoDB Atlas URL to connect Python to MongoDB
    CONNECTION = "mongodb+srv://TeamIBEA:blackwingsIBEA23@ibeacluster.x8zz5s2.mongodb.net/test"

    # create connection using MongoClient
    client = MongoClient(CONNECTION)

    # create database
    return client["IBEA_db"]

if __name__ == "__main__":
    db = get_database()

# API key (remove later): KFsjMFgrzublYYoSArwur561LNkXrHjnQp5781ciVy3FvsLtlFXZpvcVXH6Kq8DE