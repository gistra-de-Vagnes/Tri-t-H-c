# Philosophy Forum - Development Guide

This document provides instructions for setting up and developing the Philosophy Forum application.

## Project Overview

Philosophy Forum is a Django-based web application that provides:

- A database of philosophers with biographies, works, and key ideas
- Discussion forums organized by philosophy schools
- User authentication and profiles
- Vintage minimalist design with responsive layout

## Technology Stack

- **Backend**: Django 5.x
- **Frontend**: HTML5, Tailwind CSS, Alpine.js
- **Database**: SQLite (development), PostgreSQL (production)
- **Authentication**: Django built-in authentication

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Initial Setup

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
├── philosophy/          # Main Django project settings
├── philosophers/        # Philosopher database and views
│   ├── management/      # Custom management commands
│   ├── migrations/     # Database migrations
│   └── templates/      # App-specific templates
├── chat/               # Discussion forum functionality
│   ├── migrations/     # Database migrations
│   └── templates/      # App-specific templates
├── templates/          # Base templates and shared templates
├── static/             # Static files (CSS, JS, images)
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## Development Workflow

### Creating New Features

1. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```

2. Make your changes to the codebase

3. Run tests to ensure nothing is broken:
   ```bash
   python manage.py test
   ```

4. Commit your changes:
   ```bash
   git add .
   git commit -m "Description of changes"
   ```

5. Push to the repository:
   ```bash
   git push origin feature-name
   ```

### Database Changes

When making model changes:

1. Update the model in `models.py`

2. Create a migration:
   ```bash
   python manage.py makemigrations
   ```

3. Apply the migration:
   ```bash
   python manage.py migrate
   ```

### Template Development

Templates are located in:
- `templates/` - Base templates
- `philosophers/templates/` - Philosopher app templates
- `chat/templates/` - Discussion forum templates

Templates use:
- Django template language
- Tailwind CSS for styling
- Alpine.js for interactivity

### Static Files

Static files (CSS, JavaScript, images) should be placed in the `static/` directory.

## Testing

Run all tests:
```bash
python manage.py test
```

Run tests for a specific app:
```bash
python manage.py test philosophers
python manage.py test chat
```

## Deployment

For production deployment:

1. Set `DEBUG = False` in settings
2. Configure a production database (PostgreSQL)
3. Set up proper static file serving
4. Configure environment variables for secrets
5. Use a production web server (nginx, Apache, etc.)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Write tests if applicable
5. Commit your changes
6. Push to your fork
7. Create a pull request

## Troubleshooting

### Common Issues

1. **Module not found errors**: Ensure virtual environment is activated
2. **Database errors**: Run migrations with `python manage.py migrate`
3. **Static files not loading**: Run `python manage.py collectstatic`

### Getting Help

- Check the Django documentation: https://docs.djangoproject.com/

- Consult the project README.md for general information