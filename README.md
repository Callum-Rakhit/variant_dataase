#Variant DB

## Overview

This is a small web app and database for storing variants, produced by
Callum Rakhit, Stewart O'Neill and Chris Corbin.
It was built in a limited time for an MSc project by people who were learning 
Django for the first time - please do not use it diagnostically!

It is based on a blog project by Dusan Reljic.
 
It uses: Python 3.6, Django, SQLite and Bootstrap.

## What does it do?

Functionalities are:
    Upload a single variant via form
    Batch-upload variants in TSV format via file upload

The web app will have form validation, and it is planned to add checks
which prevent duplicates of the same variant record being uploaded

##Running

Run migrations:
```bash
$ python manage.py migrate
```

Initialize data:
```bash
$ python manage.py loaddata users posts comments
```

Run server on specified port:
```bash
$ python manage.py runserver <port>
```


## Post Installation

Go to the web browser and visit `http://localhost:8000/home`

Admin username: **admin**

Admin password: **adminpassword**


### Django Admin

It is possible to add additional admin user. Run the following command:
```bash
$ python manage.py createsuperuser
```