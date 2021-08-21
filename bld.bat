@echo off
set FLAG=%1

if exist build\ (
    rmdir /s /q build
)

if exist dist\ (
    rmdir /s /q dist
)

cd utils
if exist utils_lib.egg-info\ (
    rmdir /s /q utils_lib.egg-info
)

cd ..

python setup.py sdist bdist_wheel

if "%FLAG%"=="p" (
    twine upload dist/*
)
