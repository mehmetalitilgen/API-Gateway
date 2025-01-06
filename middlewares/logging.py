import logging
from datetime import datetime

logger = logging.getLogger("api_gateway")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)

def log_middleware(request, response):
    request_data = None
    try:
        if request.method in ["POST", "PUT", "PATCH"] and request.content_type == "application/json":
            request_data = request.get_json()
    except Exception:
        request_data = None

    log_data = {
        "time": datetime.now().isoformat(),
        "method": request.method,
        "path": request.path,
        "request_data": request_data,
        "status_code": response.status_code,
        "response": response.get_data(as_text=True)
    }
    logger.info(log_data)
    return response
