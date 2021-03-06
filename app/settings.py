import os

os.environ['TZ'] = 'UTC'            # zona horaria UTC

TITLE = os.getenv('K_SERVICE', 'Local')
VERSION = os.getenv('K_REVISION', 'local')
LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')

FIREBASE_WEB_API_KEY = os.environ.get('FIREBASE_WEB_API_KEY')
