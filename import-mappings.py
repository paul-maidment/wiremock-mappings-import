import sys
import json
import requests

print('Number of arguments:', len(sys.argv), 'arguments.')
wireMockHost = sys.argv[1]
wireMockPort = sys.argv[2]
wireMockUrl = 'http://' + wireMockHost + ':' + wireMockPort + '/__admin/mappings'

wiremockMappingsFile = open('wiremock-mappings.json')
wiremockMappingsJson = json.load(wiremockMappingsFile)
for jsonMapping in wiremockMappingsJson['mappings']:
	del jsonMapping['id']
	# print(json.dumps(jsonMapping))
	# print("\n")
	print(requests.post(wireMockUrl, data = json.dumps(jsonMapping)).json())
	




