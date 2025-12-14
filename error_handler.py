# error_handler.py
import logging
import traceback
from datetime import datetime
from flask import jsonify
from werkzeug.exceptions import HTTPException

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def _format_response(message, status=500, details=None):
    body = {
        "status": "error",
        "message": message,
        "details": details,
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }
    response = jsonify(body)
    response.status_code = status
    return response

def register_error_handlers(server):
    """
    Register centralized error handlers on the Flask `server` (Dash.server).
    Call this after `server = app.server` in both app_student.py and app_mentor.py.
    """

    # Handle HTTPExceptions (like abort(404) or Werkzeug HTTP exceptions)
    @server.errorhandler(HTTPException)
    def handle_http_exception(e):
        # Use e.description or e.name/detail
        message = getattr(e, "description", None) or getattr(e, "name", "HTTP error")
        status_code = getattr(e, "code", 500)
        logger.warning(f"HTTPException: {status_code} - {message}")
        return _format_response(message=message, status=status_code, details=None)

    # 404 specifically (optional; fallback already covered by HTTPException)
    @server.errorhandler(404)
    def not_found(e):
        return _format_response(message="Resource not found", status=404)

    # Generic uncaught exceptions -> 500 (log full traceback)
    @server.errorhandler(Exception)
    def handle_exception(e):
        # Log full traceback to server logs for maintainers
        tb = traceback.format_exc()
        logger.exception("Unhandled exception caught by centralized handler:\n" + tb)
        # Return safe message to client
        return _format_response(message="Internal server error", status=500)
