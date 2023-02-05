from get_database import get_database

# Get database
db = get_database()

# Create a new collection
collection = db["events"]

# Print out event details
event_details = collection.find()
for event in event_details:
    print(event["_id"], event["event_name"])