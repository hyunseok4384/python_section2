import sys
import io
import urllib.request as dw

#adsasd
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
print("Hi")

imgUrl="http://blogfiles.naver.net/20120923_166/ahnsuyeon920_134840415691074Fw5_JPEG/63.jpg"
htmlURL = "http://google.com"

savePath1="c:/test1.jpg"
savePath2="c:/index.html"

dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlURL, savePath2)

print("다운로드 완료!")
