# Create Your Own Website!

We will be leveraging Python and a web framework called [Django](https://www.djangoproject.com/) to create a simple website.
![My Website](./images/sample-website.png)

## Installing Django
First we need to install the django framework for Python using the terminal in the bottom of VSCode
```
pip install django
```

## Create the Django Project
We need to create a project directory
```
cd Desktop
mkdir django-tutorial
cd django-tutorial
django-admin startproject mysite django-tutorial
```

## Open your project in VSCode
We are now ready to open our project:
1. Select File (top left menu)
2. Open Folder
3. Select Desktop
4. Click project folder (django-tutorial)
5. Click Open

Your project should look like:
```
django-tutorial/
   manage.py
   mysite/
      __init__.py
      settings.py
      urls.py
      wsgi.py
```
Let's take a look at what each of these files is doing:
- **manage.py** - Command line utility lets you interact with your Django project.

- **\_\_init\_\_.py** –  a blank Python script whose presence indicates to the Python interpreter that the directory is a Python package.

- **settings.py** – Contains the configuration settings for the Django project.

- **urls.py** – Contains URL patterns for the Django project.

- **wsgi.py** – Contains WSGI configuration properties for the Django project.

## Testing our Application
We are now ready to start our web application for the first time!
```
python manage.py runserver 8080
```
This will start the Django's built-in server now open your preferred browser and navigate to this address http://127.0.0.1:8080/ 

if everything went well you should see the default Django's welcome page.
![Default Website](./images/django-default.png)
