from flask import request, abort
from utils.config import API_KEY
import hmac
import logging

# ---------------------------
# Logger setup
# ---------------------------
logger = logging.getLogger(__name__)


def require_api_key():
    # Get API key from request headers
    client_key = request.headers.get("X-API-Key")

    # Check if key is missing
    if not client_key:
        logger.warning("Unauthorized access attempt - missing API key")
        abort(401, description="API key missing")

    # Secure comparison to prevent timing attacks
    if not hmac.compare_digest(client_key, API_KEY):
        logger.warning("Forbidden access - invalid API key")
        abort(403, description="Invalid API key")