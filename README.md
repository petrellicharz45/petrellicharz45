User Management API
This project provides a RESTful API for managing users using Django and serialization. It allows for creating, editing, and deleting users through HTTP requests. The API follows the principles of RESTful architecture, providing endpoints for each operation.

Features
Create User: Add new users to the system by sending a POST request to the appropriate endpoint.
Edit User: Update existing user information using a PUT request with the user ID and updated data.
Delete User: Remove a user from the system by sending a DELETE request with the user ID.
Endpoints
Create User: /create/
Edit User: /users/<user_id>/update/
Delete User: /users/<user_id>/delete/
Technologies Used
Django: The web framework used to build the API.
Django REST Framework: Provides tools for building RESTful APIs in Django.
Serialization: Used to convert Django model instances into JSON data for communication over HTTP.
Bootstrap: Front-end framework for styling HTML elements.
Usage
To use the API, send HTTP requests to the specified endpoints using tools like curl, Postman, or any programming language's HTTP client library.

Example:
Create User:
bash
Copy code
POST /create/

{
    "username": "john_doe",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "is_staff": true,
    "is_active": true,
    "password": "password123",
    "is_superuser": false
}

Edit User:
bash
Copy code
PUT /users/123/update/

{
    "username": "john_doe_updated",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john_updated@example.com",
    "is_staff": true,
    "is_active": true,
    "password": "new_password123",
    "is_superuser": false
}

Delete User:
bash
Copy code
DELETE /users/123/delete/

Setup
To set up the project locally, follow these steps:

Clone the repository: git clone https://github.com/petrellicharz45/petrellicharz45.git
Install dependencies: pip install -r requirements.txt
Run migrations: python manage.py migrate
Start the development server: python manage.py runserver
License
This project is licensed under the MIT License.
