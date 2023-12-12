# Django CRM

This project is a Customer Relationship Management (CRM) system built using Django 5.0.

## Features

- **User Authentication:** Register and login users.
- **Customer Records:** Add, view, update, and delete customer records.

## Local Run

1. Clone the repository.
2. Create a virtual environment and install dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Unix/Mac
    venv\Scripts\activate     # For Windows
    pip install -r requirements.txt
    ```

3. Run migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Start the development server:

    ```bash
    python manage.py runserver
    ```