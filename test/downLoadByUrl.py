#!/usr/bin/python3
# e.g.http://app.so.com/
#download file from selected url
import urllib.request
url="http://shouji.360tpcdn.com/180822/aa171e9134dfa23c1d22a182ecf6d50c/com.ss.android.article.video_268.apk"
downPath='..\\apk\s.apk'#这里要写明名字，不能只写路径，注意\有转义的意思
urllib.request.urlretrieve(url,downPath)



