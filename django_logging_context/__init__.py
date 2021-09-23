import django

if django.VERSION < (3, 2, 0):
    default_app_config = 'django_logging_context.apps.AppConfig'  # noqa: pylint=invalid-name
