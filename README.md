# SimpleSocial - Social Networking App

![Python](https://img.shields.io/badge/python-3.9-blue.svg)
![Django](https://img.shields.io/badge/django-3.2-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

## Introduction

SimpleSocial is a full-stack social networking web application built with Django. It allows users to sign up, create interest groups, and interact with other users within these groups. Users can join existing groups, post updates, comment on posts, and more. The app aims to provide a simple and intuitive platform for users to connect and share their interests.

## Features

- User authentication and account management
- Create and join interest groups
- Post updates, images, and links
- Like and comment on posts
- View posts and activities within groups
- User profiles with bio and avatar
- Responsive and mobile-friendly design

## Requirements

- Python 3.9 or higher
- Django 3.2 or higher
- Pillow library for image handling
- Whitenoise for serving static files (optional, for production)

Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Getting Started
1. Clone the repository:
```bash
git clone https://github.com/M-Rb3/simplesocial.git
cd simplesocial
```

2. Set up a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
cd simplesocial
```

4. Apply the database migrations:
```bash
python manage.py migrate
```

## Usage
1. Start the development server:
```bash
python manage.py runserver
```
2. Open your web browser and visit http://localhost:8000 to access the SimpleSocial app.

3. Register as a new user, create interest groups, join existing groups, and start interacting with other users.

## Deployment (Optional)
To deploy SimpleSocial for production, you can use platforms like Heroku, AWS, or any other hosting service. For serving static files, you can use Whitenoise.

1. Set DEBUG=False in settings.py to disable debugging in production.

2. Install Whitenoise and add it to MIDDLEWARE in settings.py:
```python 
MIDDLEWARE = [
    # ...
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ...
]
```
3. Configure your production database in settings.py, such as PostgreSQL.

4. Deploy the app according to the platform's instructions.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
