from get_database import get_database

# Get database
db = get_database()

# Create collection for events
events_collection = db["events"]

# Insert new event to the collection
def insert_new_event(event_name, user_id, registrations, event_date, location):
    events_collection.insert_one({
        "event_name": event_name,
        "user_id": user_id,
        "registrations": registrations,
        "event_date": event_date,
        "location": location
    })

# Dummy events
user_id1 = "1"
insert_new_event("Test Event", user_id1, 0, "2023-02-05T00:00:00.000Z", "None")
user_id2 = "2"
insert_new_event("Pottery Class", user_id2, 0, "2023-04-01T16:00:00.000Z", "Greensboro, NC")