# My Django Project

A Django web application featuring a home page, user authentication system, and admin interface.

## Features

- **Home Page**: Public landing page with conditional content based on user login status.
- **Login System**: User authentication with login/logout functionality.
- **Admin Access**: Django admin interface for managing site content.

## Setup

1. Ensure Python and Django are installed.
2. Navigate to the project directory.
3. Activate the virtual environment: `.\.venv\Scripts\Activate.ps1` (Windows).
4. Apply migrations: `python manage.py migrate`
5. Create a superuser: `python manage.py createsuperuser` (or use the provided admin account).

## Running the Server

Run `python manage.py runserver` and visit `http://127.0.0.1:8000/`.

## Admin Access

- URL: `http://127.0.0.1:8000/admin/`
- Username: `admin`
- Password: `admin`

## Project Structure

- `myapp/`: Main application with views, templates, and URLs.
- `myproject/`: Django project settings and configuration.