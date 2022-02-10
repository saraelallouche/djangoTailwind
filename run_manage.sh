echo "Running makemigrations"
python manage.py makemigrations
echo "Running migrate"
python manage.py migrate
echo "Running server"
python manage.py runserver