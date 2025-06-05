import requests
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv
import csv
import time

load_dotenv()

url = os.getenv("BASE_URL")

create_user_url = f"{url}/rest/api/3/user"
search_user_url = f"{url}/rest/api/3/user/search?query="

if not url:
    raise ValueError("Missing Create User Url in .env")

jira_email = os.getenv("JIRA_EMAIL")

if not jira_email:
    raise ValueError("Jira email is not found in .env file")

API_TOKEN = os.getenv("JIRA_API_TOKEN")

if not API_TOKEN:
    raise ValueError("API_TOKEN is missing in .env file")

auth = HTTPBasicAuth(jira_email, API_TOKEN)

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

with open("users.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        email = row['emailAddress']
        name = row['displayName']
        product = row['products']

        search_response = requests.request(
                "GET",
                search_user_url + email,
                headers=headers,
                auth=auth
            )

        if search_response.status_code != 200:
            print(f"Failed to search the {email}: {search_response.text}")
            continue
        
        existing_user = search_response.json()
        if existing_user:
            print(f"The {email} is already exist, so skipping to recreate it")
            continue

        payload = json.dumps({
            "emailAddress": email,
            "displayName": name,
            "notification": True,
            "products": [product] if product else []
         })

        create_response = requests.request(
            "POST",
            create_user_url,
            data=payload,
            headers=headers,
            auth=auth
        )

        if create_response.status_code == 201:
            print(f"{name} is created successfully")
        else:
            print(f"Failed to create {name} {email} : {create_response.status_code} {create_response.text}")

            try:
                print(json.dumps(create_response.json(), indent=4))
            except json.JSONDecodeError:
                pass

        time.sleep(1)

