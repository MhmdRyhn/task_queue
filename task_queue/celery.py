# Start Celery Worker:
# celery -A task_queue worker -l info


import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_queue.settings')

celery_app = Celery('celery_playground')
celery_app.config_from_object('django.conf:settings')
