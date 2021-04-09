import logging
from django.core.servers.basehttp import ServerHandler
from . import tools


LOGGER = logging.getLogger(__name__)


class LoggingWSGIMiddleware:

    def __init__(self, application):
        self.application = application

    def __call__(self, environ, start_response):
        for chunk in self.application(environ, start_response):
            yield chunk
        if not isinstance(start_response.__self__, ServerHandler):
            request = tools.get_django_request()
            response = tools.get_django_response()
            if request and response:
                content_length = response.get('content-length')
                server_protocol = request.environ.get('SERVER_PROTOCOL')
                LOGGER.info(
                    f'"{request.method} {request.path} {server_protocol}"'
                    f' {response.status_code} {content_length}')
