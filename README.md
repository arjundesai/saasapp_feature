# SaaS Subscription Service
This project is a simple SaaS subscription service built using Flask and SQLite. It provides an API that allows users to subscribe to a service and manage their subscription status. The application is built with modular design using Blueprints, Pydantic for data validation, and SQLAlchemy for data persistence.

## Features
User can subscribe to a service by providing their name, email, and selected subscription plan.
User can query their subscription status using their email.
Data validation using Pydantic.
Subscription data is stored in an SQLite database.
## Tech Stack
Flask: Web framework for Python.
Flask-SQLAlchemy: ORM for SQLite database interactions.
Pydantic: For validating incoming API requests.
SQLite: Lightweight database to store subscription data.
## Prerequisites
To set up and run this project locally, you need the following installed on your machine:

Python 3.8+
pip (Python package manager)

## Setup and Installation
1. Clone the repository:

`git clone https://github.com/arjundesai/saas-subscription-service.git`.  
`cd saas-subscription-service`

2. Create a virtual environment (optional but recommended):

`python -m venv venv`  
`source venv/bin/activate`  # On Windows, use `venv\Scripts\activate`

3. Install the required dependencies:

`pip install -r requirements.txt`  
If the requirements.txt file doesn't exist yet, you can create it using the following command:  
`pip freeze > requirements.txt`

4. Run the Flask application:

`python app.py`  
The application will be running at http://127.0.0.1:5000.

## Configuration
The application uses an SQLite database that will automatically be created when the app runs for the first time. Configuration for the database connection is in the config.py file.

. Database: The SQLite database file (subscriptions.db) will be created in the root directory.
You can modify the database connection string in the config.py file:

`SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'subscriptions.db')`

## API Endpoints
1. Subscribe to a plan (POST /subscribe)
This endpoint allows a user to subscribe to a service by providing their details.

- **URL**: /subscribe  
- **Method**: POST  
- **Payload (JSON)**:
```json
{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "subscription_plan": "Pro"
}
```
## **Responses**:
`201 Created:`
```json
{ "message": "Subscription created successfully!" }
```
`400 Bad Request: Email is already subscribed`.
```json
{ "error": "Email already subscribed" }
```
`422 Unprocessable Entity: Missing or invalid fields.`
```json
{ "error": "Validation error details" }
```

2. Check Subscription Status (GET /subscription-status/<email>)
This endpoint returns the subscription status of a user based on the provided email.

**URL:** `/subscription-status/<email>`  
**Method:** GET  
**Responses:**  
`200 OK:`
```json
{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "subscription_plan": "Pro",
    "is_active": true
}
```
`404 Not Found:`
```json
{ "error": "Subscription not found" }
```
## Data Validation with Pydantic
We are using Pydantic for validating incoming data for the /subscribe endpoint. If the request body contains invalid or missing fields, a validation error response is returned with a 422 status code.

Example of validation errors:

```json
{
    "error": [
        {
            "loc": ["body", "email"],
            "msg": "value is not a valid email address",
            "type": "value_error.email"
        }
    ]
}
```
## Database Schema
The database schema includes a single Subscription model with the following fields:

- **id:** Unique identifier (integer, primary key).  
- **name:** Name of the subscriber (string).  
- **email:** Email address of the subscriber (string, unique).  
- **subscription_plan:** The subscription plan (e.g., "Basic", "Pro", "Enterprise") (string).  
- **is_active:** Boolean value representing if the subscription is active or not (default: True).  

## Testing the API
You can test the API using cURL, Postman, or any other API client.

Example: Subscribing a user
```bash
curl -X POST http://127.0.0.1:5000/subscribe \
    -H "Content-Type: application/json" \
    -d '{"name": "Alice", "email": "alice@example.com", "subscription_plan": "Pro"}'
```
Example: Checking subscription status
```bash
curl http://127.0.0.1:5000/subscription-status/alice@example.com
```
## Running in Production  
For running the app in a production environment, consider using a production-ready WSGI server such as Gunicorn or uWSGI.

Example using Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 app:app
```
You can then set up a reverse proxy with Nginx or Apache for serving the app.

**License**
This project is licensed under the MIT License. See the LICENSE file for details.

**Contributing**
Feel free to fork the project and submit pull requests. Please ensure code adheres to the Python PEP 8 style guide and includes relevant tests for new features.

**Contact**
If you have any questions or issues, feel free to contact me at arjunrdesai@outlook.com.

**Acknowledgments**
- Flask Documentation
- Pydantic Documentation
- SQLAlchemy Documentation
