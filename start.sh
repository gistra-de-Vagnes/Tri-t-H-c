#!/bin/bash

# Philosophy Chat - Startup Script

echo "Philosophy Chat - Starting Application"
echo "======================================"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
    echo "Virtual environment created!"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Check if database exists
if [ ! -f "db.sqlite3" ]; then
    echo "Initializing database..."
    python manage.py migrate
    echo "Database initialized!"
    
    echo "Loading sample data..."
    python manage.py init_data
    echo "Sample data loaded!"
else
    echo "Database already exists. Skipping initialization."
fi

# Start the development server
echo "Starting development server..."
echo "Access the application at http://127.0.0.1:9000/"
python manage.py runserver 9000