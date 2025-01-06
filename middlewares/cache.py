import redis
from api_gateway.utils.redis_config import get_redis_client

redis_client = get_redis_client()


def get_from_cache(key):
    value = redis_client.get(key)
    if value:
        return value.decode("utf-8")
    return None


def set_to_cache(key, value, expire=60):
    redis_client.set(key, value, ex=expire)
