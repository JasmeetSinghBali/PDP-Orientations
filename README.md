# PDP-Orientations

**BASICS OF DJANGO(covered in warehousefront dir)**

> Django (Server side framework)

**to build web apps(precisely servers) fast as F**

> Has Core Features prebuilt

1. admin site
2. ORM(object relational mapper) [helps abstracting out querying and persisting the DB without writing long complex SQL queries or schema's]
3. Authentication
4. Caching

> 🏷 Dev Notes

- pip install pipenv
  helps to install/manage dependency in virtual environment so that the depedndendcy do not clash with other project dependency

- add vs code Python(microsoft) intellisense extension

🎯 1. Creating django project

- mkdir warehousefront
- cd warehousefront
- pipenv install django (will create a virtual env and install django inside of this environment)

and a Pipfile and pipfile.lock that is like package.json and .lock file for javascirpt in json.

🎯 2. Activate the virtual env created by pipenv

- cd warehousefront
- pipenv shell
- to exit from virtual pipenv just enter "exit"

**using django-admin is kinda cli to work with django projects**

- django-admin startproject projectName . (. specifies use the current directory as our project directory)

            __init__.py defines warehouse directory as package

            settings.py to define settings for the application
            urls.py to define url of the application
            asgi & wsgi.py used for deployement

            manage.py is a wrapper around django-admin

- **IMP📝 so manage.py can be used now instead of django-admin this is important as manage.py takes settings of this project into account**

🎯 3. Running the server

            cd warehousefront
            python manage.py runserver (by default runs on port 8000)

            # python manage.py runserver PORTNUMBER(if u want to run it on specific port)

🎯 4. Integrating vs code with pipenv to run our project

            cd warehousefront
            pipenv --venv

            # copy the path and open the pallet-> python interpreter
            # enter interpreter path->paste the path
            and append at last /bin/python (in windows use \ instead of /)

- now each time you open terminal in vs code it will automatically activate the virtual env for the project warehousefront.

🎯 5. python project is a collection of multiple apps

- check the settings.py
- sessions can be removed as it is legacy

🎯 6. creating another app in warehousefront

- pipenv shell
- python manage.py startapp playground

> **NOTE- every time new app is created it has to be registered in the settings.py of the main app built in our case warehouse->settings.py under INSTALLED_APPS as string in the list**

🎯 7. writing views(request handler in django)

- views is a function that takes a request & returns a response
- though view in other architecture is that user sees while in django what user sees is called template.

- check views.py in playground

🎯 8. mapping urls to views(request handler in django)

- **📝 IMP so when that url is hit that view function is called**
- create a new file called urls.py inside playground

🎯 9. handling templates in django to return html to client(THOUGH ENTERPRISE GRADE WE RARELY OR NEVER RETURN HTML FROM SERVER TO CLIENT)

- new templates folder in playground dir

🎯 10. install django-debug-toolbar

(NOTE- DONT USE PIP USE PIPENV)
ref: https://django-debug-toolbar.readthedocs.io/en/latest/installation.html

- cd warehousefront
- pipenv shell
- pipenv install django-debug-toolbar
- mention 'debug_toolbar' in list of INSTALLED_APPS section in setting.py warehouse
- add the url path('**debug**/', include('debug_toolbar.urls')),
  in urls.py warehousefront settings.py
