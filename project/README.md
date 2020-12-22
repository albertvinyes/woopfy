#Installation
## Linux Packages
You will need to install Python 3.8, Python's dev tools and Django 3.0. You can run the following commands on Ubuntu:
```
sudo apt-get install python3
sudo apt-get install python3-pip
sudo apt-get install python3-pip
sudo apt-get install python3.8-venv
```
## Project installation
After that, clone the repository and create a virtual environment inside the woopfy folder.
```
cd /path/to/git/project/
python3 -m venv venv
```
Activate environment and install project dependencies into project dependencies.
```
source venv/bin/activate
```
Now install and setup your DB with PostgreSQL and follow the django cities light installation guide here:
https://django-cities-light.readthedocs.io/en/latest/index.html

After that install the project dependencies. If the following command runs into issues use the requirementsTest.txt file instead.
$ pip install -r requirements.txt

# Prepare the project DB and super admin
```
cd project/
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

Congrats! If everything went well you can now run tests and start playing with the software.

# Run tests and start the webserter
```
python manage.py test -v 2
python manage.py runserver
```
You can now visit the URL localhost:8000/admin and log in using the superuser credentials you just used.
