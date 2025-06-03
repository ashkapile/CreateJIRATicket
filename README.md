This project is a great template to automate the JIRA ticket


# Manage Secrets #

✅ 1. Use Environment Variables (Recommended) Set your token in the environment (not in the code):

📍Step 1: Set the token (OS-dependent)

On Linux/macOS (bash):
bash

export JIRA_API_TOKEN="your-api-token"

On Windows (Command Prompt):
cmd

set JIRA_API_TOKEN=your-api-token On Windows (PowerShell):

powershell
$env:JIRA_API_TOKEN="your-api-token"

📍Step 2: Access in Python

python
import os API_TOKEN = os.getenv("JIRA_API_TOKEN")

if not API_TOKEN: raise ValueError("API token not found in environment variable JIRA_API_TOKEN")

✅ 2. Use a .env File with python-dotenv

This is especially useful for local development.

📍Step 1: Install python-dotenv bash

pip install python-dotenv 📍Step 2: Create a .env file (same directory as your script) ini

JIRA_API_TOKEN=your-api-token

📍Step 3: Load the token in Python python

from dotenv import load_dotenv import os

load_dotenv() # Load variables from .env

API_TOKEN = os.getenv("JIRA_API_TOKEN")

if not API_TOKEN: raise ValueError("Missing API token in .env")

✅ 3. Use a Secrets Manager (for production) For serious projects or production systems, use:

AWS Secrets Manager

HashiCorp Vault

Azure Key Vault

Google Secret Manager

This approach requires cloud configuration but provides strong security controls.

❌ Avoid These (Insecure): Hardcoding the API token directly in your script

Uploading .env or config files with secrets to version control (e.g., GitHub)

 