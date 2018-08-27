__author__ = 'wyj'
#!/usr/bin/python3
from urllib import  request
from urllib import parse
from urllib import error
from http import cookiejar

def getCookeis():
    #declare a cookiejar object instance to save cookie
    cookie=cookiejar.CookieJar();
    #create cookie processor by HTTPCookieProcessor object of urllib.request lib
    handler=request.HTTPCookieProcessor(cookie);
    #create opener
    opener=request.build_opener(handler);
    #open web page
    response=opener.open('http://www.baidu.com')
    for item in cookie:
        print('Name=%s' %item.name)
        print('Value=%s' %item.value)

def getCookiesToTxt():
    filename = '..\\file\cookie.txt'
    cookie = cookiejar.MozillaCookieJar(filename)
    handler=request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    #ignore_discard:even if the cookie will be discared, it will be preserved
    #ignore_expires:if cookies exits in the file,overwrite the original file
    cookie.save(ignore_discard=True, ignore_expires=True)

def getCookiesFromTxt():
    filename = '..\\file\cookie.txt'
    #create MozillaCookieJar instance object
    cookie = cookiejar.MozillaCookieJar()
    #get cookie from the file to variables
    cookie.load(filename, ignore_discard=True, ignore_expires=True)
    handler=request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    print(response.read().decode('utf-8'))

def simulateLogin():
    #login url
    login_url = 'http://www.jobbole.com/wp-admin/admin-ajax.php'
    #User-Agent infromation
    user_agent = r'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
    #Headers information
    head = {'User-Agnet': user_agent, 'Connection': 'keep-alive'}
    #login Form_Data information
    Login_Data = {}
    Login_Data['action'] = 'login:'
    Login_Data['domain'] = 'bjtu.edu.cn'
    Login_Data['locale'] = 'zh_CN'
    Login_Data['nodetect'] = 'false'
    Login_Data['password'] = '60362355'
    Login_Data['uid'] = '17120483'
    Login_Data['useSSL'] = 'true'
    #convert to standard format
    logingpostdata = parse.urlencode(Login_Data).encode('utf-8')
    cookie = cookiejar.CookieJar()
    cookie_support = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(cookie_support)
    req1 = request.Request(url=login_url, data=logingpostdata, headers=head)

    try:
        response1 = opener.open(req1)
        html = response1.read().decode('utf-8')
        print (html)

    except error.URLError as e:
        if hasattr(e, 'code'):
            print("HTTPError:%d" % e.code)
        elif hasattr(e, 'reason'):
            print("URLError:%s" % e.reason)
if __name__=='__main__':
    #getCookeis();
    #getCookiesToTxt();
    simulateLogin();