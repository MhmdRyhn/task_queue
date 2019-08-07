# Start Celery Worker:
# celery -A task_queue worker -l info DEBUG -E


import os

from celery import Celery

from task_queue import celery_config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_queue.settings')

celery_app = Celery()
celery_app.config_from_object(celery_config)
