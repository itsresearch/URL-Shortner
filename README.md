# URL Shortener
Django URL shortener with authentication, simple forms, and click counts.

## Features are

- Register, login, and logout
- Create short URLs
- See your URLs with click counts and created date
- Edit or delete your URLs from the dashboard

## Quickstart

1. Clone and enter the project

git clone https://github.com/yourusername/url-shortener.git
cd url-shortener

2. (Optional) Create a virtual environment

python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # macOS/Linux

3. Install dependencies

pip install -r requirements.txt

4. Migrate and run

python manage.py migrate
python manage.py runserver

Open http://127.0.0.1:8000




