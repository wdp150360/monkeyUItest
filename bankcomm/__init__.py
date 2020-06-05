from .config import hostname, port
import redis


pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
rs = redis.Redis(connection_pool=pool)

