from get_database import get_database

# Get database
db = get_database()

# Create collection for users
collection = db["users"]

user_1 = {
    "_id": "IBEAU00001",
    "username": "admin",
    "password": "admin2023",
    "email": "admin@email.com"
}

user_2 = {
    "_id": "IBEAU00002",
    "username": "alecat0305",
    "password": "IBEA2023",
    "email": "alexis.cathcart0305@gmail.com"
}

collection.insert_many([user_1, user_2])