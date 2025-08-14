@echo off
title Philosophy Forum - Startup Script

echo Philosophy Forum - Starting Application
echo ======================================

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created!
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Check if database exists
if not exist "db.sqlite3" (
    echo Initializing database...
    python manage.py migrate
    echo Database initialized!
    
    echo Loading sample data...
    python manage.py init_data
    echo Sample data loaded!
) else (
    echo Database already exists. Skipping initialization.
)

REM Start the development server
echo Starting development server...
echo Access the application at http://127.0.0.1:9000/
python manage.py runserver 9000

pause