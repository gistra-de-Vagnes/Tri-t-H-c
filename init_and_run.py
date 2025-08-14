#!/usr/bin/env python
"""
Script to initialize the database and run the Philosophy Forum development server.
"""

import os
import sys
import subprocess
import django

def init_database():
    """Initialize the database with migrations and sample data."""
    print("Initializing database...")
    
    try:
        # Run migrations
        print("Running migrations...")
        subprocess.run([sys.executable, "manage.py", "migrate"], check=True)
        
        # Load sample data
        print("Loading sample data...")
        subprocess.run([sys.executable, "manage.py", "init_data"], check=True)
        
        print("Database initialization complete!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error initializing database: {e}")
        return False

def run_server():
    """Run the Django development server."""
    print("Starting Philosophy Forum development server on port 9000...")
    print("Access the application at http://127.0.0.1:9000/")
    print("Press CTRL+C to stop the server.")
    
    try:
        # Run Django development server
        subprocess.run([sys.executable, "manage.py", "runserver", "9000"], check=True)
    except KeyboardInterrupt:
        print("\nServer stopped.")
    except subprocess.CalledProcessError as e:
        print(f"Error running server: {e}")

def main():
    """Main function to initialize and run the application."""
    print("Philosophy Forum - Initialization and Setup")
    print("=" * 40)
    
    # Set the Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'philosophy.settings')
    
    # Setup Django
    try:
        django.setup()
    except Exception as e:
        print(f"Error setting up Django: {e}")
        return
    
    # Check if database is already initialized
    from django.db import connection
    from django.core.management import execute_from_command_line
    
    # Try to initialize database
    if init_database():
        print("\n" + "=" * 40)
        run_server()
    else:
        print("Database initialization failed. Please check the errors above.")

if __name__ == "__main__":
    # Check if virtual environment is activated
    if 'VIRTUAL_ENV' not in os.environ:
        print("Warning: Virtual environment does not seem to be activated.")
        print("Consider activating it with: source venv/bin/activate (Linux/Mac) or venv\\Scripts\\activate (Windows)")
        print()
    
    main()