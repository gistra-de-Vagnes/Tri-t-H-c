@echo off
echo Starting Django with ASGI...
set DJANGO_SETTINGS_MODULE=philosophy.settings
daphne -p 9000 philosophy.asgi:application