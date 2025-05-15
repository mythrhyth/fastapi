# FastAPI Health Records API

This is a simple FastAPI app to manage users and their health records. It uses SQLAlchemy for ORM and SQLite as the database.

## Features

* Create and read users
* Create and read health records linked to users
* CORS enabled for all origins
* Auto-generated API docs with Swagger UI

## Requirements

* Python 3.8+
* See `requirements.txt` for dependencies

## Installation

1. Clone this repository:

```bash
git clone https://your-repo-url.git
cd fast  # assuming the root folder is named 'fast'
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the App

Start the FastAPI server with:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

## API Documentation

Visit the interactive docs:

```
http://127.0.0.1:8000/docs
```

You can test all endpoints here.

## Usage

### Create a user

Send a `POST` request to `/users/` with JSON body:

```json
{
  "name": "Alice",
  "email": "alice@example.com"
}
```

### Create a health record

Send a `POST` request to `/records/` with JSON body:

```json
{
  "user_id": 1,
  "weight": 65.0,
  "height": 170.0,
  "blood_pressure": "120/80"
}
```

### Get user info

Send a `GET` request to `/users/{user_id}`.

### Get health records for a user

Send a `GET` request to `/records/{user_id}`.

## Viewing the Database

The app uses SQLite and stores data in `test.db`. You can open this file with any SQLite viewer, e.g., [DB Browser for SQLite](https://sqlitebrowser.org/).
