import sys
import logging
import app.settings as settings

LOGGER = logging.getLogger('fastapi')
LOGGER.setLevel(settings.LOG_LEVEL)
LOGGER.addHandler(logging.StreamHandler(sys.stdout))
