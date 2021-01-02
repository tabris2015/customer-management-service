import os
import sys
from google.cloud import firestore
from app.logs import LOGGER

if os.getenv('FIRESTORE_EMULATOR_HOST'):
    LOGGER.info('using firestore emulator')

# Project ID is determined by the GCLOUD_PROJECT environment variable
if "pytest" in sys.argv[0]:
    # testing db
    from mockfirestore import MockFirestore
    db = MockFirestore()
else:
    # not a testing db
    db = firestore.Client()  # pragma: no cover
