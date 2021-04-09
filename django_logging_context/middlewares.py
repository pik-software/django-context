import logging
from time import time

from . import tools


LOGGER = logging.getLogger(__name__)


class LoggingContextMiddleware:

    SKIPPED_MEDIA_TYPES = ('text/html', 'text/javascript')

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        LOGGER.debug(
            f'{request.method} {request.build_absolute_uri()} BODY:'
            f" {request.body.decode('utf-8', errors='ignore')}")
        tools.set_django_request(request)
        return self.process_response(self.get_response(request))

    def process_response(self, response):
        tools.set_django_response(response)
        request_start_time = tools.get_request_start_time()
        if request_start_time:
            tools.set_response_duration(time() - request_start_time)

        content_type = response._headers.get('content-type') # noqa: pylint=protected-access
        if content_type:
            media_type = content_type[1].split(';')[0]
            if media_type in self.SKIPPED_MEDIA_TYPES:
                return response

        result = []

        def log_streaming_content(content):
            for chunk in content:
                result.append(chunk.decode('utf-8', errors='ignore'))
                yield chunk

        if response.streaming:
            response.streaming_content = log_streaming_content(
                response.streaming_content)
        else:
            result.append(response.content.decode('utf-8', errors='ignore'))

        LOGGER.debug(f"RESPONSE: {''.join(result)}")
        return response
