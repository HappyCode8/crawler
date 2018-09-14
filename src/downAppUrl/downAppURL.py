__author__ = 'wyj'
#!/usr/bin/python3
from urllib import  request
import re
import json

def downUrlHomePage():
    url='http://app.so.com/';
    response = request.urlopen(url);
    html = response.read();
    html = html.decode("utf-8");
    ph_re = re.compile(r'http://.+.apk');
    matchs2 = ph_re.findall(html);
    #print (matchs2.__len__())
    #print(matchs2)
    downPath='..\\apks\\';
    for i in range(0,1):
        request.urlretrieve(matchs2[i],downPath+str(i)+'.apk')

csid={11,12,13,14,15,16,17,18,19,20,102235,102228,102139,102231,102230,102257,102256,102111,102234,102233,102232}
def downUrlOfApp():
    for cs in csid:
     for page in range (1,25):
        Request_URL='http://app.so.com/category/cat_request?page='+str(page)\
            +'&requestType=ajax&_t=1535420403039&cid=3&csid='+str(cs)+'&order=download';
        response = request.urlopen(Request_URL);
        html = response.read().decode('utf-8');
        appInformation = json.loads(html);
        filename='..\\file\\'+str(cs)+'.json';
        with open(filename, "a", encoding='utf-8') as f:
            f.write(json.dumps(appInformation, indent=4,ensure_ascii=False)[1:-1])

if __name__=="__main__":
    #downUrlHomePage();
    downUrlOfApp();