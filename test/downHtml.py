#!/usr/bin/python
#get html page from selected url
from urllib import request

response = request.urlopen("http://app.so.com")
html = response.read()
html = html.decode("utf-8")
print(html)