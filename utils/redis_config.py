import redis
from api_gateway.config import Config

def get_redis_client():
    try:
        return redis.StrictRedis(
            host=Config.REDIS_HOST,
            port=Config.REDIS_PORT,
            db=Config.REDIS_DB,
            decode_responses=True
        )
    except redis.ConnectionError:
        raise Exception("Redis connection failed")
