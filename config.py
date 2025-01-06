import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-key")
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    REDIS_DB = int(os.getenv("REDIS_DB", 0))
    SERVICE_URLS = [
        os.getenv("SERVICE_1"),
        os.getenv("SERVICE_2"),
        os.getenv("SERVICE_3")
    ]
    LOAD_BALANCER_STRATEGY = os.getenv("LOAD_BALANCER_STRATEGY", "round_robin")  # round_robin, random, least_connections
