'''
Created on 2018年12月10日

@author: cy
'''
import redis
import chardet


class RedisTools(object):
    def __init__(self, **params):
        host = params.get('host', 'localhost')
        port = params.get('port', 6379)
        db = params.get('db')
        pool = redis.ConnectionPool(host=host, port=port)
        self.redis = redis.Redis(connection_pool=pool)

    def get_port_by_username(self, username):
        try:
            ret = self.redis.get(username)
            port = self.decode(ret)
            port = int(port)
        except Exception as e:
            port = None
        return port

    def set(self, key, value):
        try:
            ret = self.redis.get(key)
            if ret:
                raise Exception('key已存在')
            ret = self.redis.set(key, value)
        except Exception as e:
            print(str(e))
            ret = -1
        return ret

    @staticmethod
    def decode(value):
        character = chardet.detect(value).get('encoding')  # chardet.detect检测的字符串越长越准确，越短越不准确。
        value = value.decode(character)
        return value


myRedis = RedisTools()
