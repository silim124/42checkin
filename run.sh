#!/bin/sh

# please check if you are in the '42check_in' directory now

# Check the code for PEP8 requirements
flake8

# run 42check_in server
python manage.py runserver
