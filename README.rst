This is a django project. To use this project, you would need Python 3.6
or higher and django 2.0.4.

##Recommendation 

For ease of use, it is recommended that you install a
virtual environment, run

``pip install virtualenv virtualenvwrapper-win``

To create a new virtual environment, run ``mkvirtualenv envname`` and to
activate the virtual environment, run ``workon envname``

##Get Started 

To install dependencies, run

``python setup.py install``

To start the server, run

``python manage.py runserver``

To add more apps to the project, just run

``django-admin startapp appname``

and make sure to add it to the installed apps in the project’s
``settings.py`` file

To start a new project, run ``django-admin startproject``

There are three models namely, ``ScrumyUser``, ``GoalStatus`` and
``ScrumyGoals``