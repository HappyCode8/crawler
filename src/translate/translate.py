#To get specific translation from youdao dictionary
from urllib import request
from urllib import parse
import json

def youdaoTranslte(content):
    #Request URL,http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
    #need delete '_o' from the real request url
    Request_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    #form data
    Form_Data = {}
    # Form_Data['action'] = 'FY_BY_REALTIME'
    # Form_Data['client'] = 'fanyideskweb'
    Form_Data['doctype'] = 'json'#can't delete,return type
    # Form_Data['from'] = 'AUTO'
    Form_Data['i'] = content#can't delete,what you want to translate
    # Form_Data['keyfrom'] = 'fanyi.web'
    # Form_Data['salt'] = '1535095852800'
    # Form_Data['sign'] = '0171c905bdec8ebc0c4d5886d2654d40'
    # Form_Data['smartresult'] = 'dict'
    # Form_Data['to'] = 'AUTO'
    # Form_Data['typoResult'] = 'false'
    # Form_Data['version']='2.1'
    #encode to utf-8
    data = parse.urlencode(Form_Data).encode('utf-8')
    #get response and decode
    response = request.urlopen(Request_URL,data)
    html = response.read().decode('utf-8')
    #get json data
    translate_results = json.loads(html)
    #get the results and print them
    translate_results = translate_results['translateResult'][0][0]['tgt']
    print("the translate result is:%s" % translate_results)

def baiduTranslate(content):
    #http://fanyi.baidu.com/v2transapi,replace v2transapi with transapi
    Request_URL='http://fanyi.baidu.com/transapi'
    # Form_data={}
    # Form_data['from']='zh'#from what language,can't delete
    # Form_data['query']=content
    # Form_data['sign']=31275.301338
    # Form_data['simple_means_flag']=3
    # Form_data['to']='en'#translate to what language,can't delete
    # Form_data['token']='2f0475fd14bf2db3efd5758867e3b56e'
    # Form_data['transtype']='translang'
    Form_data={'from':'zh','query':content,'to':'en'}
    data=parse.urlencode(Form_data).encode('utf-8')
    response=request.urlopen(Request_URL,data)
    print (response)
    html=response.read().decode('utf-8')
    translate_results = json.loads(html)
    translate_results = translate_results['data'][0]['dst']
    print("the translate result is:%s" % translate_results)

if __name__ == "__main__":
    #youdaoTranslte('猫和狗')
    baiduTranslate('我家养了一只猫')