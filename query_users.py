from get_database import get_database

# Get database
db = get_database()

# Create a new collection
collection = db["users"]

# Print out user details
user_details = collection.find()
for user in user_details:
    print(user["_id"], user["username"])