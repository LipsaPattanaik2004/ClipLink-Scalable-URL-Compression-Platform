from cache.redis_client import redis_client

LIMIT = 5
WINDOW = 60  # seconds

def is_allowed(ip):
    key = f"rate:{ip}"
    count = redis_client.get(key)

    if count and int(count) >= LIMIT:
        return False

    pipe = redis_client.pipeline()
    pipe.incr(key, 1)
    pipe.expire(key, WINDOW)
    pipe.execute()

    return True
