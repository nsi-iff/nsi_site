NSI Site
========

How to Install
--------------

Your system need to have at least python2.6 and same native dependencies, for installing them:

    $ apt-get install python-dev
    $ apt-get install libxml2 libxslt1.1 libxslt1-dev

For installing all dependencies::

    $ pip install -r requirements.txt


Developers should add any new dependency to requirements.txt file::

    $ pip freeze > requirements.txt

