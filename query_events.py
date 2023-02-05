from get_database import get_database

# Get database
db = get_database()

# Access events collection
events_collection = db["events"]

# Print out event details
event_details = events_collection.find()
for event in event_details:
    print(event["_id"], event["event_name"])