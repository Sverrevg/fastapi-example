import logging

from starlette.testclient import TestClient

from src.app import app

logger = logging.getLogger(__name__)
logger.disabled = True

client = TestClient(app)
