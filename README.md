# Introapp

## Description

This project provides a simple API that returns basic information, including the current date and time, an email address, and a GitHub URL. The API is designed to be used as part of a backend service and can be accessed via a GET request to the `/api/intro/` endpoint.

## Setup Instructions

To run this project locally, follow these steps:

### Prerequisites

- Make sure you have Python 3.12.7++ installed on your local machine.

### Steps to Set Up Locally

1. **Clone the repository:**

   First, clone the repository to your local machine using:

   ```bash
   git clone <repository_url>
   cd <project_directory>
   ```

2. **Create a virtual environment:**

   It's recommended to use a virtual environment for this project. You can create one with the following command:

   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies:**

   Use the `requirements.txt` file to install all necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**

   Now, you can run the Django application locally:

   ```bash
   python manage.py runserver
   ```

6. **Access the API:**

   Your application should now be running at `http://127.0.0.1:8000/`. The `/api/intro/` endpoint can be accessed at:

   ```
   http://127.0.0.1:8000/api/intro/
   ```

## API Documentation

### Endpoint: `/api/intro/`

- **Request:**

  - **Method:** GET
  - **URL:** `/api/intro/`
  - **Request Body:** None

- **Response Format:**
  The response will be in JSON format and will include the following fields:

  ```json
  {
    "email": "email@example.com",
    "current_datetime": "2025-01-29T16:21:01Z",
    "github_url": "https://github.com/example"
  }
  ```

  - **email:** A string containing the email address.
  - **current_datetime:** A string containing the current UTC date and time in ISO 8601 format.
  - **github_url:** A string containing the URL to the GitHub profile or repository.

### Example Usage

To get the information, send a GET request to the following URL:

```
GET http://127.0.0.1:8000/api/intro/
```

**Sample Response:**

```json
{
  "email": "email@example.com",
  "current_datetime": "2025-01-29T16:21:01Z",
  "github_url": "https://github.com/example"
}
```

## Backlink

If you're looking to hire a Python developer, check out this [Python Developer Hiring page](https://example.com/hire-python-developer).
