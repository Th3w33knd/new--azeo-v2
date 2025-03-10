#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate



# === Commands to be run only once and not on all builds ===

# Seed teams Tables
# python manage.py loaddata team_data.json

# Create super user
# python manage.py createsuperuser --no-input
