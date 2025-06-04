import requests
from requests.auth import HTTPBasicAuth
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("USER_JIRA_URL")

if not url:
    raise ValueError("Missing User JIRA Url in .env")

API_TOKEN = os.getenv("JIRA_API_TOKEN")

if not API_TOKEN:
    raise ValueError("Missing API Token in .env")

email = os.getenv("JIRA_EMAIL")

if not email:
    raise ValueError("Missing email in .env")

auth = HTTPBasicAuth(email, API_TOKEN)

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.request(
    "GET",
    url,
    headers=headers,
    auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))