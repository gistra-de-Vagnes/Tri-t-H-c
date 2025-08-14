#!/usr/bin/env python
"""
Script to run the Philosophy Forum development server.
"""

import os
import sys
import subprocess

def run_server():
    """Run the Django development server."""
    print("Starting Philosophy Forum development server on port 9000...")
    print("Press CTRL+C to stop the server.")
    
    try:
        # Run Django development server
        subprocess.run([sys.executable, "manage.py", "runserver", "9000"], check=True)
    except KeyboardInterrupt:
        print("\nServer stopped.")
    except subprocess.CalledProcessError as e:
        print(f"Error running server: {e}")
    except FileNotFoundError:
        print("Error: Could not find manage.py. Make sure you're in the project directory.")

if __name__ == "__main__":
    # Set the Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'philosophy.settings')
    
    # Check if virtual environment is activated
    if 'VIRTUAL_ENV' not in os.environ:
        print("Warning: Virtual environment does not seem to be activated.")
        print("Consider activating it with: source venv/bin/activate (Linux/Mac) or venv\\Scripts\\activate (Windows)")
    
    run_server()