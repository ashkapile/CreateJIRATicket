import requests
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv
import time
import csv

load_dotenv()

url = os.getenv("BASE_URL")

create_user_url = f"{url}/rest/api/3/user"
search_user_url = f"{url}/rest/api/3/user/search?query="

if not url:
    raise ValueError("Missing Create User Url in .env")

jira_email = os.getenv("JIRA_EMAIL")

if not jira_email:
    raise ValueError("Missing email in .env")

API_TOKEN = os.getenv("JIRA_API_TOKEN")

if not API_TOKEN:
    raise ValueError("Missing API Token in .env")

auth = HTTPBasicAuth(jira_email, API_TOKEN)

users_to_create = [
    {
        "emailAddress": "johndoe@gmail.com", 
        "displayName": "John Joe", 
        "notification": True, 
        "products": ["jira-software"]
    },
    {
        "emailAddress": "abc@gmail.com", 
        "displayName": "Alex", 
        "notification": True, 
        "products": ["jira-software"]
    }
]

headers = {
    "Accept": "application/json",
    "Content-Type" : "application/json"
}

for user in users_to_create:
    email = user["emailAddress"]

    search_response = requests.get(search_user_url + email, headers=headers, auth=auth)

    if search_response.status_code != 200:
        print(f"Failed to search user {email}: {search_response.text}")
        continue

    existing_users = search_response.json()
    if existing_users:
        print(f"User {email} is already exist. Skipping the invitation.")
        continue

    payload = json.dumps({
        "emailAddress": email,
        "displayName": user["displayName"],
        "notification": True,
        "products": user["products"]
    })

    invite_response = requests.request(
        "POST",
        create_user_url,
        data=payload,
        headers=headers,
        auth=auth
    )

    if invite_response.status_code == 201:
        print(f"Invited {email}")

    else:
        print(f"❌ Failed to invite {email} (Status {invite_response.status_code}):")
        print(json.dumps(invite_response.json(), indent=4))

    time.sleep(1)

