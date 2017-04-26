# Automation
Automation of Examination Cell SET activities

### Installing Python Packages

```
$ git clone git@github.com:PunitGr/AESSET-server.git
$ cd automation

$ sudo easy_install pip

$ pip install virtualenv
$ pip install virtualenvwrapper

$ source virtualenvwrapper.sh
$ mkvirtualenv --python=/usr/bin/python3 automation

$ workon automation

(automation)$ pip install -r requirements.txt
```

### Setting Up PostgreSQL
* Install PostgreSQL first:

_Linux users:_

```
$ sudo apt-get update
$ sudo apt-get install postgresql postgresql-contrib
```

_Mac users:_


```$ brew install postgresql```
 to install latest version of Postgresql.


After completing installation run the following commands. We are going to create a new user and database for AESSET,

```
$ sudo -u postgres psql

postgres=# CREATE DATABASE auto;
postgres=# CREATE ROLE automation WITH LOGIN;
postgres=# ALTER ROLE automation WITH PASSWORD 'auto1!';
postgres=# GRANT ALL ON DATABASE auto TO automation;
```


### Creating Schema
Once we have Django app and Postgresql installed it's now time to create the schema and the superuser.

```
(automation)$ ./manage.py migrate
(automation)$ ./manage.py createsuperuser
```

#### Note
Whenever you install add a package using pip don't forget to update requirements.txt. Update requirements by typing pip freeze>requirements.txt

#### Documentation

* **[Seating Manager](https://github.com/PunitGr/AESSET-server/blob/master/docs/seatingmanager.md)**
* **[Query Manager](https://github.com/PunitGr/AESSET-server/blob/master/docs/querymanager.md)**