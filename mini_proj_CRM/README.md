> # CRM via django

> few imp extensions vscode

- django by Robert Solis for pre-built snippet of blocks,filters,forms, models, models field etc...

- django template by bibhasdn , template language support for python highlighting

> core setup

virtualenv just like pipenv that creates virtual env that holds all dependencies of the project in django

- pip install virtualenv (if already installed pipenv skip this step)

            # cd to project directory

            # create the virtual environment
            # note env can be any other arbitary name also
            virtualenv env

            # in case of mac
            source env/bin/activate

            # in case of windows
            ref: https://www.liquidweb.com/kb/how-to-setup-a-python-virtual-environment-on-windows-10/

            <path to project>\env\Scripts\activate.bat

- **u will see (env) now with the terminal in the current dir**

            # install django inside env
            pip install django (or pip install django==3.1.4 to install exact version of django)

- **To check all the dependency were installed properly we can output all the dependancy list in file**

            # output all installed depend in file
            pip freeze > installedDependencies.txt

- **create the CRM project directory**

            # create new project
            django-admin startproject lacrm .

- **add .gitignore ref:https://github.com/github/gitignore/blob/main/Python.gitignore**

> server & migrations

(inside virtual env in project folder to activate /pathtoproj/scripts/activate.bat)

- run django server at default localhost:8000

            # runserver at 8000 (inside env)
            python manage.py runserver

- migrations helps to apply any changes that are their to the database.

            # migrations (inside env)
            python manage.py migrate

- django by default have dbsqlite3 configuration at the starting as db.

            # runserver
            python manage.py runserver

            # no warnings now

> project structure

                # helps to identify this project as module
                __init__.py

                # helps to run the django server asynchronously
                asgi.py

                # whiskey.py file (generally used in combination of asgi.py while deploying)
                wsgi.py

                # settings of entire project
                # configuring templates,database connection, installed apps

Notes

- secret key mentioned in settings.py should be loaded as system env in production

- DEBUG = False when in production env

- ALLOWED_HOSTS refers to the domain where this project is allowed to be hosted on like 'mydomain.com' no need of http or https just domain name is enough

- INSTALLED_APPS where new apps can be added that we create.
- MIDDLEWARES coming from django
- ROOT_URL_CONF points to the project urls.py
- TEMPLATES config having DIRS that is list of directories, so if different folder/dirs signfies the templates in different folders then those dirs/folder need to specify in DIRS list in settings.py
- DATABASE configuration section that points to the dbsqlite3 by default can be changed a/c to the database configuration wheather its postgreSQL or mariaDB.
- AUTH_PASSWORD_VALIDATORS to validate auth password validator
- timezones configs
- static urls

> Project walkthorugh

- Leads app - as the CRM revolve arounds managing leads.

                # inside project dir (virtualenv activated)
                python manage.py startapp leads
