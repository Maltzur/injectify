help:
	@echo "init - initialize and install virtual environment"
	@echo "clean - remove artifacts"
	@echo "test - run all tests"
	@echo "coverage - check code coverage"
	@echo "publish - package and upload a release"
	@echo "docs - generate Sphinx HTML documentation"

init:
	pip install pipenv --upgrade
	pipenv install --dev

clean-tox:
	rm -fr .tox/

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type f -name '*.py[co]' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean: clean-tox clean-build clean-pyc

test:
	# This runs all of the tests.
	detox

ci:
	pipenv run pytest -n 8 --boxed --junitxml=report.xml

lint:
	pipenv run flake8 injectify tests

coverage:
	pipenv run pytest --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov=injectify tests

publish:
	pip install 'twine>=1.5.0'
	python setup.py sdist bdist_wheel
	twine upload dist/*
	rm -fr build dist .egg injectify.egg-info

.PHONY: docs
docs:
	cd docs && make html
	@echo "\033[95m\n\nBuild successful! View the docs homepage at docs/_build/html/index.html.\n\033[0m"
