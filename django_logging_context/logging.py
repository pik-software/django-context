import logging

from . import tools


LOGGER = logging.getLogger(__name__)


class ContextExtendingFilter(logging.Filter):

    def filter(self, record):
        record.request_id = tools.get_request_id()
        record.user_id = tools.get_user_id()
        record.username = tools.get_username()
        record.remote_addr = tools.get_remote_addr()
        response_duration = tools.get_response_duration()
        request = tools.get_django_request()
        if request and request.build_absolute_uri:
            record.uri = request.build_absolute_uri()
        if response_duration is not None:
            response_duration = '{0:0.6f}s'.format(response_duration)
        record.response_duration = response_duration
        return True
