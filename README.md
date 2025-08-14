# Philosophy Forum

A vintage minimalist website for philosophical discourse with discussion forums dedicated to different schools of philosophy.

## Features

- **Philosopher Database**: Browse information about famous philosophers including biographies, key works, and ideas
- **Vintage Minimalist Design**: Clean, elegant interface with a vintage aesthetic
- **Discussion Forums**: Interactive discussion forums for each philosophy school
- **User Authentication**: Registration and login system with user profiles
- **Search & Filtering**: Find philosophers by name, school, country, or time period
- **Markdown Support**: Format your discussion posts with Markdown syntax

## Technology Stack

- **Backend**: Django 5.x
- **Frontend**: HTML5, Tailwind CSS, Alpine.js
- **Database**: SQLite (development), PostgreSQL (production)
- **Authentication**: Django built-in authentication
- **Deployment**: Railway/Heroku/VPS

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd philosophy-chat
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run database migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Load sample data** (optional):
   ```bash
   python manage.py init_data
   ```

7. **Create a superuser** (optional):
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the development server**:
   ```bash
   python manage.py runserver 9000
   ```

9. **Access the application** at `http://127.0.0.1:9000/`

## Project Structure

```
philosophy-chat/
├── philosophy/              # Main Django project settings
├── philosophers/            # Philosopher database and views
│   ├── management/          # Custom management commands
│   │   └── commands/       # Custom management commands
│   ├── migrations/         # Database migrations
│   └── templates/          # App-specific templates
├── chat/                   # Real-time chat functionality
│   ├── migrations/         # Database migrations
│   └── templates/          # App-specific templates
├── templates/              # Base templates and shared templates
├── static/                 # Static files (CSS, JS, images)
│   └── css/                # Custom CSS styles
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
└── DEVELOPMENT.md         # Development guide
```

## Chat Rooms

The application includes dedicated chat rooms for various philosophy schools:

- Stoicism
- Existentialism
- Rationalism
- Empiricism
- Ancient Greek Philosophy
- Analytic Philosophy
- And more...

Users can join any room to discuss philosophical ideas with other enthusiasts.

## Deployment

This application can be deployed to:

- Railway
- Heroku
- Any VPS with Python/Django support

For production deployment, make sure to:

1. Set `DEBUG = False` in settings
2. Configure a production database (PostgreSQL)
3. Set up proper static file serving
4. Configure environment variables for secrets

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.