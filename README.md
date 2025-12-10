# Polar

This is a skill listing platform

## Prerequisites

- Python 3.x
- pip
- Git

## Initial Setup

1. **Clone and navigate to the repository**
```bash
   git clone <repository-url>
   cd polar
```

2. **Create and checkout your feature branch**
```bash
   git checkout -b feature/<your-feature-name>
```

3. **Install pipenv** (if not already installed)
```bash
   pip install pipenv
```

4. **Activate the virtual environment**
```bash
   pipenv shell
```

5. **Install project dependencies**
```bash
   pipenv install
```

6. **Run database migrations**
```bash
   python manage.py migrate
```

## Creating a New Django App

Follow these steps when adding a new feature module:

1. **Generate the app**
```bash
   python manage.py startapp <your_app_name>
```

2. **Register the app**
   - Add your app to `INSTALLED_APPS` in `settings.py`

3. **Set up URL routing**
   - Create a `urls.py` file in your app folder
   - Define your app-specific URL patterns in this file
   
4. **Connect to main URL configuration**
   - In the project-level `urls.py`, add:
```python
   path('<app-url-path>/', include('<app_name>.urls', namespace='<app_name>'))
```
   
   **Example:**
```python
   path('auth/', include('authentication.urls', namespace='auth'))
```
   This makes all authentication URLs accessible at `/auth/...`

5. **Create migrations** (if you've added models)
```bash
   python manage.py makemigrations
   python manage.py migrate
```

## User Model

This project uses Django's default User model with no custom fields.

**To import:**
```python
from django.contrib.auth.models import User
```

## Development Workflow

- Always work on a feature branch
- Run migrations after pulling updates that include model changes
- Test your changes before committing

---

Happy coding! 🚀