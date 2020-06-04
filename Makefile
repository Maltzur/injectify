PYPI_SERVER = testpypi

NC= \033[0m
RED = \033[0;31m
GREEN = \033[0;32m
BLUE = \033[0;34m

init:
	@echo "+ $@"
	@pip install pipenv --upgrade
	@pipenv install --dev

.PHONY: clean-tox
clean-tox:
	@echo "+ $@"
	@rm -fr .tox/

.PHONY: clean-build
clean-build:
	@echo "+ $@"
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

.PHONE: clean-pyc
clean-pyc:
	@echo "+ $@"
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type f -name '*.py[co]' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +

.PHONY: clean
clean: clean-tox clean-build clean-pyc

.PHONY: build
build:
	@echo "+ $@"
	@pipenv run python setup.py sdist bdist_wheel

.PHONY: test
test:
	# This runs all of the tests.
	@echo "+ $@"
	@detox

.PHONY: ci
ci:
	@echo "+ $@"
	@pipenv run pytest --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov=injectify tests

.PHONY: test-readme
test-readme:
	@echo "+ $@"
	@$(MAKE) build
	@echo "${BLUE}"
	@pipenv run twine check dist/*
	@echo "${NC}"
	@$(MAKE) clean-build

.PHONY: lint
lint:
	@echo "+ $@"
	@pipenv run flake8 injectify tests

.PHONY: coverage
coverage:
	@echo "+ $@"
	@pipenv run pytest --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov=injectify tests

.PHONY: publish
publish:
	@echo "+ $@"
	@$(MAKE) build
	@pipenv run twine upload -r ${PYPI_SERVER} dist/*
	@$(MAKE) clean-build

.PHONY: docs
docs:
	@echo "+ $@"
	@cd docs && pipenv run make html
	@echo "\033[95m\n\nBuild successful! View the docs homepage at docs/_build/html/index.html.\n\033[0m"
