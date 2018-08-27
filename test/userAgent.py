#!/usr/bin/python3
from urllib import request

def urlWithOutSettingAgent():
    url = 'http://www.csdn.net/'
    req = request.Request(url)
    response = request.urlopen(req)
    html = response.read().decode('utf-8')
    print(html)

def urlWithSettingAgent():
    url = 'http://www.csdn.net/'
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) ' \
                         'AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  ' \
                         'Safari/535.19'
    req = request.Request(url, headers=head)
    response = request.urlopen(req)
    html = response.read().decode('utf-8')
    print(html)

def urlWithSettingAgent2():
    url = 'http://www.csdn.net/'
    req = request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) '
                                 'AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 '
                                 ' Safari/535.19')
    response = request.urlopen(req)
    html = response.read().decode('utf-8')
    print(html)

if __name__=="__main__":
    #urlWithOutSettingAgent();
    #urlWithSettingAgent()
    urlWithSettingAgent2()