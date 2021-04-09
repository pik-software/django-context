from . import tools


def request_started_handler(sender, **kwargs):
    tools.set_request_id()
    tools.set_request_start_time()


def request_finished_handler(sender, **kwargs):
    tools.clear_storage()
