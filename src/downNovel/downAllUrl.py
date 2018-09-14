__author__ = 'wyj'

from urllib import request
from bs4 import BeautifulSoup
#down all chapters url
if __name__ == "__main__":
    target_url = 'https://www.9dxs.com/0/680/index.html'
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    target_req = request.Request(url = target_url, headers = head)
    target_response = request.urlopen(target_req)
    target_html = target_response.read().decode('gbk','ignore')
    listmain_soup = BeautifulSoup(target_html,'lxml')
    chapters = listmain_soup.find_all('div',class_ = 'chapterlist')
    download_soup = BeautifulSoup(str(chapters), 'lxml')
    begin_flag=False
    for child in download_soup.ul.children:
        if child!='\n':
            if child.string=='章节目录':
                begin_flag=True
            if begin_flag==True and child.a!=None:
                download_url='https://www.9dxs.com/0/680/'+child.a.get('href')
                download_name=child.string
                print(download_name+':'+download_url)


