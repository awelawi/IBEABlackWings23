import requests
import json
url = "https://data.mongodb-api.com/app/data-qevcc/endpoint/data/v1/action/findOne"

payload = json.dumps({
    "collection": "users",
    "database": "IBEA_db",
    "dataSource": "IBEACluster",
    "projection": {
        "_id": 1
    }
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': "IBEADatabaseKey", 
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
