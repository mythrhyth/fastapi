import requests

# List of users to add
users = [
    {"name": "Bob", "email": "bob@example.com"},
    {"name": "Charlie", "email": "charlie@example.com"},
    {"name": "Diana", "email": "diana@example.com"}
]

# Endpoint for creating users
url = "http://127.0.0.1:8000/users/"

# Send POST request for each user
for user in users:
    response = requests.post(url, json=user)
    if response.status_code == 200:
        print(f"✅ Created user: {response.json()}")
    else:
        print(f"❌ Failed to create user {user['email']} – {response.status_code}: {response.text}")
