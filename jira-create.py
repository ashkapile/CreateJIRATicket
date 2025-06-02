import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://ashvinikapile123.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0VF3XtKvure6qTln9tf4nbyKb3d43AI8-yZNWhJMj2jAQbwBjdZfmJVDE0o82B8ydQEcomY3lVj4mcJCbOFdhDEwf0-KzMMJ2ZUbgEPXOM0TO51cskNB2FltQT-erMnamFgKRdOB05w0Fw8-qO0gg29s3bbQxa6rGr3uqBF1ZGn8=C2B37181"

auth = HTTPBasicAuth("ashvinikapile123@gmail.com", API_TOKEN)

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

