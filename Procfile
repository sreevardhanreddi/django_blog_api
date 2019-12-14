web:python manage.py runserver
web:python manage.py makemigrations
web:python manage.py migrate
web:python manage.py seed_data_to_db
web: gunicorn django_blog_api.wsgi --log-file -
heroku ps:scale web=1