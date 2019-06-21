import logging
from django.conf import settings


class MyErrorFilter(logging.Filter):

    def filter(self, record):
        if record.args[1].startswith('404'):
            return True
        if record.args[1].startswith('/errors/404'):
            return True
        if record.args[1].startswith('500'):
            return True
        if record.args[1].startswith('/errors/500'):
            return True
        return False