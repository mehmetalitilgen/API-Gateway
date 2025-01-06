from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import redis

def setup_rate_limiter(app):
    try:
        limiter = Limiter(
            get_remote_address,
            app=app,
            default_limits=["100 per hour"],
            storage_uri=f"redis://{app.config['REDIS_HOST']}:{app.config['REDIS_PORT']}"
        )
        return limiter
    except redis.ConnectionError:
        app.logger.error("Redis connection failed. Rate limiting disabled.")
        return Limiter(lambda: None)
