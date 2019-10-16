import redis
ip = "localhost"
port = 6379
password = ""
key = "hello"
value = "world"
r = redis.Redis(host=ip, port=port, password=password, decode_responses=True)
