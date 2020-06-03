from .config import hostname, port
import redis
from bankcomm.random_num import RandomSeed
from bankcomm.config import seed

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
rs = redis.Redis(connection_pool=pool)

random_s = RandomSeed(seed)

__all__ = ['hostname', 'port']
