from celery import Celery
from src.util import config


def make_celery():
   celery = Celery(__name__, broker=config.CELERY_BROKER)
   celery.conf.update(config.as_dict())
   return celery

celery = make_celery()