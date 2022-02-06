# Django site

Tutorials used:
- https://www.youtube.com/watch?v=rHux0gMZ3Eg
- https://www.youtube.com/watch?v=ZsJRXS_vrw0

## Getting Started: 
- download django, should have pip3, python3 etc. get pip env so you can install django in an environment
- `pip3 install pipenv`, `pipenv install django` --> should give you a virtual path
- `python3 manage.py runserver` to start server. should auto-reload update when you make and save changes

<br>
<br>
<br> 


# starting fresh -- Rena's tutorial notes
`pip3 install pipenv`
`mkdir storefront`
`cd storefront`
`pipenv install django` # —> should give you path to virtual env

`pipenvshell` # —> run interpreter in shell

`django-admin startproject storefront .` #  —> django-admin gives us commands

#### go in manage.py for settings …. is like a dj admin

#### run server: 
python3 manage.py runserver # opt supply port number

to get integrated terminal —> but i think not anymore just slect it
$pipenv --venv # then get path + /bin/python

#settings > installed apps > delete sessions app — not rly needed 

#### open new terminal window
`python3 manage.py startapp <name>` ( new app has folder with specific structure  )
- apps are like config
- model classes pull out data, tests, views (request handler)

#### create new app—> add `<name>` to settings
create view

# File Structure
### views are request handlers
create view.py and add a fxn ….

-  map url to view …. w url.py
-  then import to main url config

### templates — return templates to return html content
render fxn remders template and returns html markup to client
won’t use templates bc we don’t just want to render html content

### debugging django by installing degub toolbar  — open run and debug panel, create launch profile, django… launch.json
- add port  9000
- can add break point, start app for debugging, etc etc
- see variables, watch, things to run fxns etc easily
- `python3 -m pip install django-debug-toolbar`
- `pipenv install django-debug-toolbar`
- add to settings, installed apps ‘debug_toolbar’
- then go to urls.py in store front folder
- add middleware to settings mod
- config internal ips

# using db -->  sqllite
- need `migrate python3 manage.py migrate`
- add 'myapp' to settings.py
- create class in models.py in user
- then register table with django admin system
— import and add to admin

### migration : description on how to change db models to app models
- `python3 manage.py makemigrations <app-name>`
- all db changes are now in 0001 file (each time you add a model you get 0002, 0003, etc

- `python3 manage.py sqlmigrate user 0001`
##### apply changes
- `python3 manage.py migrate user`
#### now db and description are up to date together

#### create admin user in db
- renarepenning@gmail.com
- pword: `capstone`
- **i had to go back and make migrations!**
- `python3 manage.py migrate`
- `python3 manage.py makemigrations`

### adding table
- make one in  model
- add to admin
- python3 manage.py makemigrations user
- python3 manage.py migrate user 0002
- python3 manage.py migrate user

— variables harvested to url —> fxn in view —> then object to model 


# heroku
installing heroku brew install heroku/brew/heroku

