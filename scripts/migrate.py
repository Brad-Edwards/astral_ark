#!/usr/bin/env python

import os

os.system("docker-compose -f local.yml run --rm django python manage.py migrate")
