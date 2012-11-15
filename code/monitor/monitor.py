
import redis


if __name__ == '__main__':

    rc = redis.Redis(host='alvarolizama.net')
    ps = rc.pubsub('status')
    rc.publish('status', 'hello world')
