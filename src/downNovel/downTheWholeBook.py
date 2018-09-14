__author__ = 'wyj'
from urllib import request
from bs4 import BeautifulSoup
import sys

if __name__ == "__main__":
    file = open('唐砖.txt', 'w', encoding='utf-8')
    target_url = 'https://www.9dxs.com/0/680/index.html'

    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'

    target_req = request.Request(url = target_url, headers = head)
    target_response = request.urlopen(target_req)
    target_html = target_response.read().decode('gbk','ignore')
    listmain_soup = BeautifulSoup(target_html,'lxml')
    chapters = listmain_soup.find_all('div',class_ = 'chapterlist')
    download_soup = BeautifulSoup(str(chapters), 'lxml')
    numbers = (len(download_soup.ul.contents) - 1) / 2 - 8
    index = 1
    begin_flag = False
    begin_flag = False
    for child in download_soup.ul.children:
        if child != '\n':
            if child.string == '章节目录':
                begin_flag = True
            if begin_flag == True and child.a != None:
                download_url = 'https://www.9dxs.com/0/680/' + child.a.get('href')
                download_req = request.Request(url = download_url, headers = head)
                download_response = request.urlopen(download_req)
                download_html = download_response.read().decode('gbk','ignore')
                download_name = child.string
                soup_texts = BeautifulSoup(download_html, 'lxml')
                texts = soup_texts.find_all(id = 'content', class_ = 'content')
                soup_text = BeautifulSoup(str(texts), 'lxml')
                write_flag = True
                file.write(download_name + '\n')
                #将爬取内容写入文件
                #将爬取内容写入文件
                for each in soup_text.div.text.replace('\xa0',''):
                    if each == 'h':
                        write_flag = False
                    if write_flag == True and each != ' ':
                        file.write(each)
                    if write_flag == True and each == '\r':
                        file.write('\n')
                file.write('\n\n')
                #打印爬取进度
                sys.stdout.write("已下载:%.3f%%" % float(index/numbers) + '\r')
                sys.stdout.flush()
                index += 1
    file.close()