import urllib.request
import datetime

class CacheEntry:
    def __init__(self, data):
        self.data = data
        self.timestamp = datetime.datetime.now().timestamp()

cache = {}

CACHE_TIMEOUT_SECS = 10

while True:

    url = input('Enter a URL:')

    if url = '':
        continue

    cur_time = datetime.datetime.now().timestamp()
    print(cur_time)

    if url not in cache or cur_time - cache[url].timestamp > CACHE_TIMEOUT_SECS: # added 2nd part to measure time since last caching of url data

        resp = urllib.request.urlopen(url)
        data = resp.read()
        # OLD
        # cache[url] = data  # and also a timestamp, tuple works, 
        # but need to know index, so use an object
        cache[url] = CacheEntry(data)
        resp.close()
        print('cache miss')
    else:
        print('cache hit')

    # print(cache[url][:75])  #OLD
    print(cache[url].timestamp)
    print(cache[url].data[:75])
