#!/usr/bin/env python3
echo "Pushing to Heroku"
git push heroku main
echo "Make migrations"
heroku run python manage.py makemigrations
echo "Migrate"
heroku run python manage.py migrate
