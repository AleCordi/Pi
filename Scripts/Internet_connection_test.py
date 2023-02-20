#!/usr/bin/env python3
import requests
import datetime
url = "https://www.google.it/"
timeout = 20
try:
	request = requests.get(url, timeout=timeout)
	content=request.content
	size=len(content)
	elapsed=request.elapsed
	print("Connected to the Internet")
	print(elapsed)
	print(request.status_code)
	print(size)
except (requests.ConnectionError, requests.Timeout) as exception:
	print("No internet connection.")