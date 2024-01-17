# Site_Nexus

comandos para ativar o ambiente virtual e ligar o servidor:

pip install virtualenv
python -m virtualenv venv
./venv/Scripts/activate
pip install django, djangorestframework, psycopg2, pillow
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
python manage.py runserver