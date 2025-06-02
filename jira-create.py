import requests
from requests.auth import HTTPBasicAuth
import json

url = "JIRA Project URL"

API_TOKEN = ""
auth = HTTPBasicAuth("email", "API_TOKEN")

headers = {
    "Accept" : "application/json",
    "Content-Type" : "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first Jira ticket of the day",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },

    "issuetype": {
      "id": "10004"
    },

    "project": {
      "key": "SCRUM"
    },

    "summary": "Main order flow broken",

    },

  "update": {}
} )


response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

