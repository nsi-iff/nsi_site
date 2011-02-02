PYTHON=python
PIP=pip

export DJANGO_SETTINGS_MODULE=settings

all: create_database migrate_database deps test 

create_database:
	@$(PYTHON) manage.py syncdb

migrate_database:
	@$(PYTHON) manage.py migrate

deps: django pil south docutils

functional_deps: lettuce splinter should-dsl nose lxml

should-dsl:
	@$(PYTHON) -c 'import should_dsl' 2>/dev/null || $(PIP) install should-dsl

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

test: functional unit

functional: functional_deps deps
	@echo ==============================================
	@echo ========= Running acceptance specs ===========
	@python manage.py harvest --settings=settings_test
	@echo

unit: deps
	@echo ==============================================
	@echo ========= Running acceptance specs ===========
	@python manage.py test
	@echo

