#!/usr/bin/env python
"""
Setup script for Philosophy Forum.
This script helps users set up the virtual environment and install dependencies.
"""

import os
import sys
import subprocess
import platform

def create_virtual_environment():
    """Create a virtual environment."""
    print("Creating virtual environment...")
    try:
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("Virtual environment created successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error creating virtual environment: {e}")
        return False

def activate_virtual_environment():
    """Provide instructions to activate the virtual environment."""
    system = platform.system()
    
    if system == "Windows":
        activate_script = "venv\\Scripts\\activate"
        print(f"\nTo activate the virtual environment, run:")
        print(f"  {activate_script}")
    else:
        activate_script = "source venv/bin/activate"
        print(f"\nTo activate the virtual environment, run:")
        print(f"  {activate_script}")
    
    print("\nAfter activation, you can install dependencies with:")
    print("  pip install -r requirements.txt")

def install_dependencies():
    """Install project dependencies."""
    print("Installing dependencies...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        return False

def main():
    """Main setup function."""
    print("Philosophy Forum - Setup Script")
    print("=" * 35)
    
    # Check if virtual environment exists
    if not os.path.exists("venv"):
        if create_virtual_environment():
            activate_virtual_environment()
    else:
        print("Virtual environment already exists.")
    
    print("\nNext steps:")
    activate_virtual_environment()
    print("  pip install -r requirements.txt")
    print("  python manage.py migrate")
    print("  python manage.py init_data")
    print("  python manage.py runserver 9000")

if __name__ == "__main__":
    main()