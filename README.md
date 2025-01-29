Project Name
Introapp.

Description
This project provides a simple API that returns basic information, including the current date and time, an email address, and a GitHub URL. The API is designed to be used as part of a backend service, and can be accessed via a GET request to the /api/intro/ endpoint.

Setup Instructions
To run this project locally, follow these steps:

Prerequisites
Make sure you have Python 3.x installed on your local machine.

Steps to Set Up Locally
Clone the repository:

First, clone the repository to your local machine using:

-> git clone <repository_url>
-> cd <project_directory>

Create a virtual environment:
It's recommended to use a virtual environment for this project. You can create one with the following command:
-> python3 -m venv venv

Activate the virtual environment:

On macOS/Linux:
-> source venv/bin/activate

On Windows:
-> venv\Scripts\activate

Install dependencies:
Use the requirements.txt file to install all necessary dependencies:

-> pip install -r requirements.txt

Run the application:
Now, you can run the Django application locally:

-> python manage.py runserver

Access the API:

Your application should now be running at http://127.0.0.1:8000/. The api/intro/ endpoint can be accessed at:

http://127.0.0.1:8000/api/intro/

API Documentation
-> Endpoint: /api/intro/
Request
-> Method: GET
-> URL: /api/intro/

No request body is needed. Simply send a GET request to the endpoint.

Response Format
The response will be in JSON format and will include the following fields:

{
"email": "email@example.com",
"current_datetime": "2025-01-29T16:21:01Z",
"github_url": "https://github.com/example"
}

-> email: A string containing the email address.
-> current_datetime: A string containing the current UTC date and time in ISO 8601 format.
-> github_url: A string containing the URL to the GitHub profile or repository.

Example Usage
To get the information, send a GET request to the following URL:

GET http://127.0.0.1:8000/api/intro/
Sample Response:

{
"email": "email@example.com",
"current_datetime": "2025-01-29T16:21:01Z",
"github_url": "https://github.com/example"
}

Backlink
If you're looking to hire a Python developer, check out this [Python Developer Hiring page](https://hng.tech/hire/python-developers).
