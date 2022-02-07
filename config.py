# configurando o mysql

cd c:/
mkdir Python
cd Python
python -m venv venv
cd venv/Scripts
activate

cd c:/
pip install django
django-admin startproject project .
python manage.py startapp app

python
pip install mysqlclient-1.4.6-cp38-cp38-win32.whl
python manage.py migrate
python manage.py runserver
pip install mysql-connector-python
