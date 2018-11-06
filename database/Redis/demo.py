from redis import StrictRedis

# db: 使用的数据库
redis = StrictRedis(host='localhost', port=6379, db=0)
redis.set('name', 'bob')
print(redis.get('name'))