#!/usr/bin/env python3
import requests
import datetime
url = "https://www.google.com"
timeout = 20
try:
	request = requests.get(url, timeout=timeout)
	content=request.content
	size=len(content)
	elapsed=request.elapsed
	print("Connected to the Internet")
	print("Elapsed time: " + str(elapsed))
	print("Request status code: " + str(request.status_code))
	print("Byte size: " + str(size))
except (requests.ConnectionError, requests.Timeout) as exception:
	print("No internet connection.")
