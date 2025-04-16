# Create Your Own Website!

We will be leveraging Python and a web framework called [Django](https://www.djangoproject.com/) to create a simple website.

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
