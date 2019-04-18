#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-04-18 10:27
@Author  : red
@Site    : 
@File    : event_knowledge_API.py
@Software: PyCharm
"""
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
	# Request headers
	'Ocp-Apim-Subscription-Key': '37484e1bbb054550b638e29ecfd856e9',
}

params = urllib.parse.urlencode({
	# Request parameters
	'expr': "And(Composite(AA.AuN=='jaime teevan'),Y>2012)",
	'model': 'latest',
	# 'attributes': '{string}',
	'count': '10',
	'offset': '0',
})


def get_data():
	try:
		conn = http.client.HTTPSConnection('api.labs.cognitive.microsoft.com')
		conn.request("GET", "/academic/v1.0/calchistogram?%s" % params, "{body}", headers)
		response = conn.getresponse()
		data = response.read()
		print(data)
		conn.close()
	except Exception as e:
		print("[Errno {0}] {1}".format(e.errno, e.strerror))


if __name__ == '__main__':
	get_data()
