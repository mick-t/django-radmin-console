import os
from setuptools import setup

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name='django-radmin-console',
    version='0.9',
    license="BSD",  
    description = '',
    author='Angel Medrano',
    author_email='asmedrano@gmail.com',
    url='https://github.com/asmedrano/django-radmin-console',
    download_url='https://github.com/asmedrano/django-radmin-console/downloads',
    include_package_data = True,    
    packages = ['radmin'],
    package_data = {'radmin': ['radamin/*']},
    classifiers=[
        'Development Status::4- Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Django Developers',
        'License :: BSD License',
        'Operating System :: OS independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
