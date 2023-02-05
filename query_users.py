from get_database import get_database

# Get database
db = get_database()

# Access users collection
users_collection = db["users"]

# Print out user details
user_details = users_collection.find()
for user in user_details:
    print(user["_id"], user["username"])