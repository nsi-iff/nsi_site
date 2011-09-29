PYTHON=python
PIP=pip

export DJANGO_SETTINGS_MODULE=settings

all: deps test_database test remove_test_database

database:
	@$(PYTHON) manage.py syncdb
	@$(PYTHON) manage.py migrate

test_database:
	@echo ==============================================
	@echo ========== Creating test database ============
	@echo
	@$(PYTHON) manage.py syncdb --settings=settings_test
	@$(PYTHON) manage.py migrate --settings=settings_test


remove_test_database:
	@echo ==============================================
	@echo ========== Deleting test database ============
	@rm nsi_site-test.db

deps: app_deps functional_deps unit_deps

app_deps: django pil south docutils django-pagination linaro_django_pagination

functional_deps: selenium lettuce splinter should-dsl nose lxml

unit_deps: should-dsl model_mommy specloud nosedjango

selenium:
	@$(PYTHON) -c 'import selenium' 2>/dev/null || $(PIP) install selenium==2.0rc3

should-dsl:
	@$(PYTHON) -c 'import should_dsl' 2>/dev/null || $(PIP) install http://github.com/hugobr/should-dsl/tarball/master

django:
	@$(PYTHON) -c 'import django' 2>/dev/null || $(PIP) install django

splinter:
	@$(PYTHON) -c 'import splinter' 2>/dev/null || $(PIP) install http://github.com/cobrateam/splinter/tarball/master

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
	@$(PYTHON) -c 'import nosedjango' 2>/dev/null || $(PIP) install -U nosedjango nose

model_mommy:
	@$(PYTHON) -c 'import model_mommy' 2>/dev/null || $(PIP) install http://github.com/vandersonmota/model_mommy/tarball/master

django-pagination:
	@$(PYTHON) -c 'import pagination' 2>/dev/null || $(PIP) install -e git+https://github.com/tiagosc/django-pagination.git#egg=pagination

linaro_django_pagination:
	@$(PYTHON) -c 'import linaro_django_pagination' 2>/dev/null || $(PIP) install -U linaro_django_pagination

test: functional unit

functional: functional_deps deps
	@echo ==============================================
	@echo ========= Running acceptance specs ===========
	@python manage.py harvest --settings=settings_test
	@echo

unit: unit_deps deps
	@echo ==============================================
	@echo ============ Running unit specs ==============
	@specloud --with-django --nocapture
	@echo

