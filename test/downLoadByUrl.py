#!/usr/bin/python3
# e.g.http://app.so.com/
#download file from selected url
import urllib.request
url="http://shouji.360tpcdn.com/180822/aa171e9134dfa23c1d22a182ecf6d50c/com.ss.android.article.video_268.apk"
downPath='..\\apks\s.apk'#include the source name，not only path，"\\"the first is the escape character
urllib.request.urlretrieve(url,downPath)



