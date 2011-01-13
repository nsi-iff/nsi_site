NSI Site
========

How to Install
--------------

Your system need to have at least python2.6 and some native dependencies, for installing them::

    $ apt-get install python-dev

    $ apt-get install libxml2 libxslt1.1 libxslt1-dev


Makefile installs the dependencies using `Pip <http://pip.openplans.org/>`_, then you have to install it (run with root privileges)::

  apt-get install python-setuptools

  easy_install pip


After install these system-related dependencies, you can run `make` to install all Python dependencies (if they are not installed) and run all tests. Depending on your environment, this script may need root permissions in order to install the dependencies.


Developers should add any new dependency to Makefile. Please
