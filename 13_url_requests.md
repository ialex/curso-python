# URL Requests #

## urllib ##

### Get ###
	import urllib2

	url = 'http://www.google.com/'
	response = urllib2.urlopen(url).read()

### Post ###

	import urllib
	import urllib2

	url = 'http://google.com/'
	params = urllib.urlencode({
  	'search': 'Hello:',
	})
	response = urllib2.urlopen(url, params)
    response.read()


## Requests ##

    pip install requests

	import requests  

	r = requests.get('https://github.com/timeline.json')
	r = requests.post("http://httpbin.org/post")
	r = requests.put("http://httpbin.org/put")
	r = requests.delete("http://httpbin.org/delete")

	payload = {'key1': 'value1', 'key2': 'value2'}
	r = requests.get("http://httpbin.org/get", params=payload)

	r.text
	r.json



<http://docs.python-requests.org/>
	
	

