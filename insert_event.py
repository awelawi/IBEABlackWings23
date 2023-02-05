from get_database import get_database

# Get database
db = get_database()

# Create collection for events
collection = db["events"]

event_1 = {
    "_id": "IBEAE00001",
    "event_name": "Test Event",
    "creator_id": "IBEA00001",
    "registrations": 0,
    "event_date": "2023-02-05T00:00:00.000Z",
    "location": "None"
}

event_2 = {
    "_id": "IBEAE00002",
    "event_name": "Pottery Class",
    "creator_id": "IBEA00002",
    "registrations": 5,
    "event_date": "2023-04-01T16:00:00.000Z",
    "location": "Greensboro, NC"
}

collection.insert_many([event_1, event_2])