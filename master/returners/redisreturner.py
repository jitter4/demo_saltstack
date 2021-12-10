import redis
import salt.utils.json


def returner(ret):
    """
    Return information to a redis server
    """
    # Get a redis connection
    serv = redis.Redis(host="redis-serv.example.com", port=6379, db="0")
    serv.sadd("%(id)s:jobs" % ret, ret["jid"])
    serv.set("%(jid)s:%(id)s" % ret, salt.utils.json.dumps(ret["return"]))
    serv.sadd("jobs", ret["jid"])
    serv.sadd(ret["jid"], ret["id"])