from django.apps import AppConfig as BaseAppConfig
from django.core.signals import request_started, request_finished

from .signals import (
    request_finished_handler, request_started_handler)


class AppConfig(BaseAppConfig):
    name = 'django_logging_context'

    def ready(self):
        request_started.connect(
            request_started_handler, dispatch_uid='request_started')
        request_finished.connect(
            request_finished_handler, dispatch_uid='request_finished')
