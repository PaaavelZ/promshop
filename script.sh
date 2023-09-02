#!/bin/bash

source /home/notroot/promshop/venv/bin/activate
python /home/notroot/promshop/manage.py makemigrations
python /home/notroot/promshop/manage.py migrate
python /home/notroot/promshop/manage.py collectstatic --no-input
sudo systemctl restart gunicorn
sudo systemctl restart nginx
