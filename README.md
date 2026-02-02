# URL Shortener

A simple Django URL shortener with user authentication, URL management, and click counts.

## Features

### Core Features

- **User Authentication**: Register, login, and logout
- **Shortening URLs**: Input long URLs and receive short links
- **URL Management**: View, edit, and delete short URLs with creation date and usage stats
- **Basic Analytics**: Click count for each short URL
- **Responsive UI**: Clean Bootstrap-based interface

### Optional Feature

- **Custom Short URLs**: Users can set custom short codes (letters, numbers, hyphens only)

## Setup

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/url-shortener.git
   cd url-shortener
   ```

2. Create and activate virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   # or: source venv/bin/activate   # Linux/Mac
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Create superuser (optional, for admin access):

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. Open http://127.0.0.1:8000 in your browser.

## Usage

1. **Register** a new account or **Login** if you have one
2. **Create** short URLs by entering a long URL (optional: custom code)
3. **Dashboard** shows all your short URLs with click counts, creation dates, and actions
4. **Edit** or **Delete** URLs from the dashboard
5. Access any short URL at `http://yoursite.com/{code}/` to redirect to the original

## Project Structure

```
shortner/
├── SHORTNER/          # Project settings
├── urlshortner/       # Main app
│   ├── models.py      # ShortURL model
│   ├── views.py       # All views
│   ├── forms.py       # Forms
│   ├── utils.py       # Short code generator
│   └── templates/     # App templates
├── templates/         # Base template
├── requirements.txt
└── README.md
```

## Technical Details

- **Short Codes**: Random short codes with a uniqueness check
- **Database**: SQLite (default), easily switchable to PostgreSQL/MySQL
- **Authentication**: Django's built-in auth system

## License

MIT
