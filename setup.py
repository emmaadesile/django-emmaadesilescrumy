import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme: 
  README = readme.read():

#allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup = (
  name = 'django-emmaadesilescrumy',
  version = '1.0.0'
  author = 'Adesile Emmanuel',
  author_email = 'emma2adesile@gmail.com',
  description = 'A django project to manage scrum tasks',
  long_description = README,
  license = 'BSD License',
  packages = find_packages(),
  include_package_data = True,
  keywords = 'python django scrum tutorial',
  url = "https://github.com/emmaadesile/django-emmaadesilescrumy",
  classifiers = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Framework :: Django :: 2.0',
    'Intended Audience :: Developers',
    'License :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.6',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
  ]
)