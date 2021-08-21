@echo off

set PYTHONPATH=%PYTHONPATH%;
pipenv run pytest
py.test --cov=./ --cov-report=html
