import redis
rc = redis.Redis(host='alvarolizama.net')

ps = rc.pubsub()
ps.subscribe(['juggernaut'])


for item in ps.listen():
    if item['type'] == 'message':
        print item['channel']
        print item['data']

