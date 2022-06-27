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
