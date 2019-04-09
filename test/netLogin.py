__author__ = 'wyj'

from urllib import request
from urllib import parse
import json

if __name__=='__main__':
    login_url='http://10.1.61.1/a70.htm'
    head={}
    head['User-Agent']='Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) ' \
                       'AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    Form_data={'0MKKey':'%B5%C7%C2%BC%28Login%29',
               'DDDDD':'17120483',
               'upass':'wyj60362355',
               'C2':'on'}
    data=parse.urlencode(Form_data).encode('utf-8')
    response=request.urlopen(login_url,data)
    print (response)
    html=response.read().decode('gb2312')
    print(html)
