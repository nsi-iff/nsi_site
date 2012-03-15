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
	@echo Deleting test database...
	@rm nsi_site-test.db

deps: app_deps functional_deps unit_deps

app_deps:
	pip install -r requirements_app.txt

functional_deps:
	pip install -r requirements_functional.txt

unit_deps:
	pip install -r requirements_unit.txt

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

run:
	@python manage.py runserver 0.0.0.0:8000
