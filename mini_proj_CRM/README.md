> # CRM via django

> few imp extensions vscode

- django by Robert Solis for pre-built snippet of blocks,filters,forms, models, models field etc...

- django template by bibhasdn , template language support for python highlighting

- sqlite by alexcvzz to explore sqlite

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

> ## Project walkthorugh

- Leads app - as the CRM revolve arounds managing leads.

                # inside project dir (virtualenv activated)
                python manage.py startapp leads

- mentione leads as installed_app in setting.py

- **django models** that refers to the representation of the database schema

- models in django are written as class

- to create schema from models.py

            (in project virtualenv active)
            python manage.py makemigrations

- migrations-> 0001_initial.py

- **📝NOTE- the migration is just a blueprint class i.e it dont effect the dbsqlite3 file at all**

> **🎯IMP: executing/running the existing migrations that has not been applied/executed/ran yet**

            (in project dir virtualenv from env/Scripts/activate/bat)
            python manage.py migrate
            # this will find all migrations in all apps and run and apply all of them that have not been applied yet.

- **📝now on opening the dbsqlite3 it will have a table named lead**

            cntrl+shift+p
            sqlite
            open database
            select the dbsqlite3 file from your project dir

            open the explorer on left
            sqlite explorer

            check for the new lead table

> Foreign Keys (Relationship managment in SQL)

- ref leads->models.py
- **📝:IMP Foreignkeys always required on_delete positional argument it tells django how to handle when the related table row or instance is deleted. for case like where we deleted an agent that belong to lead then in that case what happens to the foreign key relation**

> 📝:IMP on_delete (ref:models.py)

- **📝:IMP on_delete=models.CASCADE means if agent is deleted then the corresponding table for lead entry will also be deleted that holds the relation with the deleted agent**

- **📝:IMP on_delete=models.SET_NULL,null=True means that the forign key would be set as null for the current table to the table entry to which this foreign key reff to on deletion of that agent**

- **📝:IMP on_delete=models.SET_DEFAULT,default=someDefaultValue means that the forign key would be set as default value given for the current table to the table entry to which this foreign key reff to on deletion of that agent**

> Custom User Model (Django has lot of built in func/mech to handle authentications)

                from django.contrib.auth import get_user_model

- **But it always a good practice and also practical to customize the user model**

- **📝:IMP so inherit AbstractUserClass from django that gives a basic user class that can be further customized a/c to the needs ref: models.py**

- **📝:IMP to tell django about the user model edit the mainApp->settings.py of the project ref:settings.py**

> 📝:IMP NOTE- makes sure when u make changes to your models.py u delete the dbsqlite file & the migrations folder 0001_initial.py and so on files inside
> (in the virtual env) python manage.py makemigrations
> python manage.py migrate

- **the dependencies in migrations file say 0001_initial.py will be exected after the mentioned file in the array like in our case auth**

> QuerySets & Model Managers

- **📝: IMP to access model managers say the model class named as class Agents then Agents.objects(helps to access model manager)**

                # some methods on model manager
                # syntax- ModelClassName.objects.method(...schemaProps|| none)
                Lead.objects(firstName="john",lastName="wick",age=35)

                # QuerySets
                # query for all Lead in database
                Lead.objects.all()

                # query for Lead with age greater than 30
                Lead.objects.filter(age__gt=30)

                # query a specific firstName lead
                Lead.objects.filter(firstName="john")

- **📝:IMP a python shell can be created in django that will have access to the project**

                # in virtual (env) of the project
                /pathtoproj/env/Scripts/activate.bat
                python manage.py shell

                # importing models into the shell
                from leads.models import Lead

                # now model manager can be used to run query or apply methods on this model

                Lead.objects.all()

> 📝: IMP create first superadminuser

                # make sure you are out of python shell if not type exit()
                python manage.py createsuperuser

                # open the shell again
                python manage.py shell

                # import User model from django settings in shell
                from django.contrib.auth import get_user_model
                User = get_user_model()
                User.objects.all()

                # output
                <queryset username>(of the super user u creatd with createsuperuser command earlier)

                # cntrl + shift + p
                sqlite open connection
                choose db.sqlite3 inside project dir (mini_proj_crm)

                # go to lead_user
                and right click-> show table

                # importing Agent model and creating new Agent
                from leads.models import Agent
                # grab the superuser
                admin_user = User.objects.get(username="jassi")
                admin_user
                agent = Agent.objects.create(user=admin_user)

> 📝: IMP for getting the string representation of the model we have to define a function in models.py in Agent section with

                def __str__(self): (ref model.py)


                # exit out of shell
                exit()

                python manage.py shell

                from leads.models import Agent
                Agent.object.all()

> 🚫 conclusion: django has built in ORM to interact with object models with model manager methods & query sets without the need to write SQL queries

                # creating a new lead
                >>>from leads.models import Lead
                # ADVANCE LOOKUP WITH REF - querying the Agent model via user with __ to filter by fields
                >>>jassi_agent = Agent.objects.get(user__email="devs.us.1984@gmail.com")
                >>>jassi_agent
                >>>Lead.objects.create(first_name="jack", last_name="sparrow", age=40, agent=jassi_agent)


                # add string represent for Lead model as well via def __str__(self)
                # exit()
                python manage.py shell
                from leads.models import Lead
                Lead.objects.all()

                # output
                <jack sparrow>

> Django Admin (can be logged in by staff user or superuser)

                (in env) virtual env activate.bat
                python manage.py runserver

                # go to localhost:8000/admin
                # login via superuser creds created earlier

                # register models inside leads->admin.py
                # can be accessed/viewed via UI in built in django admin at localhost:8000/admin

> 📝: IMP Views in django (request processing handlers that return response)

- **ref: views.py in leads folder**

- function based view that handle the view

                def home_page(request):

- **to use this function it should be added to urls.py in the root app folder lacrm**

> 📝:IMP TEMPLATES in django returning html content from backend

- **ref: views.py render method**

- **📝: Way-1 IMP creating templates folder inside your app ref: leads->templates->leads as django find templates by templates->appName(folder) so no additional settings required to locate this html file/template**

- **📝: Way-2 IMP creating templates folder inside root of the django app folder templates but this is not is not discovered by django so we tell django about this so in lacrm ->settings.py**

> Context (passing information into the django template that could be used by the template then)

- we can pass context in render method itself as third paramter

            # context is just dictionalry of information
            context = {
                key: value...
            }
            return render(request, "home_page.html", context)

- smart template syntax then can be used to access context inside home_page.html template

            # syntax for accessing context inside template
            {{}}

> URL Namespaces

- for the current project the lacrm-> urls.py is the main url file that django looks at to determine the urls/routes

- **📝:IMP though each app could have their own urls.py file with urlpattern**

> arguments in path can be given ref: urls.py in leads

            # primary key as argument for differnt leads on basis of primary key
            <pk>

> Forms and create view

- the forms from django or customized one must be wrapped inside a html form tag as we want intentionally to submit this form

            <form>
                {{form}}
            </form>

- by default if the form method is post than django requires to pass the csrf_token also that handles the csrf token mitigation and adds the csrf middleware to prevent csrf attacks.

            {% csrf_token %}

> 📝: IMP Model Forms

ref: leads/forms.py , leads/views.py

- model form has form.save() all the data entered into form and then create a model and store it in db abstracting away all repeated logic that needs to be written.

- model for instance=modelInstance during populating form can be used to update a specific instance of the model ref instance=lead in leads/views.py

> URL namespace to make refferences of the route better

- helps to pass reff for routes instead of passing hardcoded full urls paths where it is required.
- ref: leads/urls.py, lead_list.py

                    # go inside leads namespace and then look for the name of url paths -> lead-create
                    # in {% %}
                    <a href="{% url 'leads:lead-create' %}">Create a new lead</a>

- in future if u want to change the name of the url u can directly change it in leads/urls.py at one place

                    # for lead-detail route
                    # {% url 'namespace:name' paramsUWantToPass %}
                    <a href="{% url 'leads:lead-detail' lead.pk %}"

> Extending templates [base template that can be inherited by other templates to avoid repetition of code]

- refer: templates/base.html

> Tailwind CSS [to base.html so that all templates can extend it]
> ref: https://tailwindcss.com/docs/installation/play-cdn
> ref: https://tailblocks.cc/

Class based-views 338
