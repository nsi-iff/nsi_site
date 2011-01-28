PYTHON=python
PIP=pip

export DJANGO_SETTINGS_MODULE=settings

all: deps test

deps: django pil south

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

lettuce:
	@$(PYTHON) -c 'import lettuce' 2>/dev/null || $(PIP) install lettuce

nose:
	@$(PYTHON) -c 'import nose' 2>/dev/null || $(PIP) install nose

lxml:
	@$(PYTHON) -c 'import lxml' 2>/dev/null || $(PIP) install lxml

test: functional

functional: functional_deps deps
	@echo ==============================================
	@echo ============ Create a database ===============
	@python manage.py migrate
	@echo ==============================================
	@echo ========= Running acceptance specs ===========
	@python manage.py harvest
	@echo

