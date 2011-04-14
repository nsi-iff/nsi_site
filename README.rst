NSI Site
========

How to Install
--------------

On Debian like
~~~~~~~~~~~~~~
Just run::

    ./setup_on_debian_like.sh

On Windows
~~~~~~~~~~
I don't know, sorry.


Python dependencies
~~~~~~~~~~~~~~~~~~~
Run::

    make deps

How to create the databases
---------------------------
Just run::

    make database

For test database, run::

    make test_database

Note: after you run functional tests, the admin user on test database will be "admin" with password "admin".

How to Run Tests
----------------
Run `make test` to install all Python dependencies (if they are not installed) and run all tests. Depending on your environment, this script may need root permissions in order to install the dependencies.

You can run `make functional` for executing only acceptance tests, and `make unit` to execute only unit tests.

Remember to install all dependencies and create the test database before run any test.

How to Contribute
-----------------
Please:
    - Fork the project and submit pull request
    - Create an issue
    - Close an issue

