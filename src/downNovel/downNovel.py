__author__ = 'wyj'
from urllib import  request
from bs4 import BeautifulSoup
#down novel by url
if __name__=='__main__':
    download_url='https://www.9dxs.com/0/680/6465625.html'
    head={}
    head['User-Agent']='Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) ' \
                       'AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    download_req=request.Request(url=download_url,headers=head)
    download_response=request.urlopen(download_req)
    download_html=download_response.read().decode('gbk','ignore')
    soup_texts=BeautifulSoup(download_html,'lxml')
    texts=soup_texts.find_all(id='content',class_='content')
    soup_text=BeautifulSoup(str(texts),'lxml')
    print(soup_text.div.text.replace('\xa0',''))