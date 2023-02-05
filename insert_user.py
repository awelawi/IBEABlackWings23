from get_database import get_database

# Get database
db = get_database()

# Create collection for users
users_collection = db["users"]

# Insert new user to the collection
# Get username, password, and email from request
def insert_new_user(username, password, email):
    users_collection.insert_one({
        "username": username,
        "password": password,
        "email": email
    })

# Dummy users
insert_new_user("admin", "admin2023", "admin@gmail.com")
insert_new_user("alecat0305", "IBEA2023", "alexis.cathcart0305@gmail.com")