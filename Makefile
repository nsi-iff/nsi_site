PYTHON=python
PIP=pip

export DJANGO_SETTINGS_MODULE=settings

all: deps test

database:
	@$(PYTHON) manage.py syncdb
	@$(PYTHON) manage.py migrate

test_database:
	@$(PYTHON) manage.py syncdb --settings=settings_test
	@$(PYTHON) manage.py migrate --settings=settings_test

deps: app_deps functional_deps unit_deps

app_deps: django pil south docutils

functional_deps: lettuce splinter should-dsl nose lxml

unit_deps: should-dsl model_mommy specloud nosedjango

should-dsl:
	@$(PYTHON) -c 'import should_dsl' 2>/dev/null || $(PIP) install http://github.com/hugobr/should-dsl/tarball/master

django:
	@$(PYTHON) -c 'import django' 2>/dev/null || $(PIP) install django

splinter:
	@$(PYTHON) -c 'import splinter' 2>/dev/null || $(PIP) install splinter

pil:
	@$(PYTHON) -c 'import pil' 2>/dev/null || $(PIP) install PIL

south:
	@$(PYTHON) -c 'import south' 2>/dev/null || $(PIP) install South

docutils:
	@$(PYTHON) -c 'import docutils' 2>/dev/null || $(PIP) install docutils

lettuce:
	@$(PYTHON) -c 'import lettuce' 2>/dev/null || $(PIP) install lettuce

nose:
	@$(PYTHON) -c 'import nose' 2>/dev/null || $(PIP) install nose

lxml:
	@$(PYTHON) -c 'import lxml' 2>/dev/null || $(PIP) install lxml

specloud:
	@$(PYTHON) -c 'import specloud' 2>/dev/null || $(PIP) install specloud --no-deps -r http://github.com/hugobr/specloud/raw/master/requirements.txt

nosedjango:
	@$(PYTHON) -c 'import nosedjango' 2>/dev/null || $(PIP) install nosedjango	
 
model_mommy:
	@$(PYTHON) -c 'import model_mommy' 2>/dev/null || $(PIP) install http://github.com/vandersonmota/model_mommy/tarball/master


test: functional unit

functional: functional_deps deps
	@echo ==============================================
	@echo ========= Running acceptance specs ===========
	@python manage.py harvest --settings=settings_test
	@echo

unit: unit_deps deps
	@echo ==============================================
	@echo ========= Running unit specs ===========
	@specloud --with-django
	@echo

