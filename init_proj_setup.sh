#!/bin/bash

# 1. Set up the Django project with 'config' as the main configuration directory
django-admin startproject config .

# 2. Set up the apps directory
mkdir apps

# 3. Navigate into the apps directory
cd apps

# 4. Create the 'main' app
django-admin startapp main

# 5. Create the 'scraper' app
django-admin startapp scraper

# 6. Navigate back to the root directory
cd ..

# 7. Set up the static directory with its subdirectories
mkdir -p static/css static/js static/images

# 8. Set up the templates directory with a global subdirectory
mkdir -p templates/global

# 9. Create a media directory for uploaded files
mkdir media

# 10. Create an .env file for environment variables (you'll populate this later)
touch .env

# 11. Create a README.md for your project documentation (you'll populate this later)
touch README.md
