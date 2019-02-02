import sys
import io
import urllib.request as dw
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


imgUrl="http://blogfiles.naver.net/20120923_166/ahnsuyeon920_134840415691074Fw5_JPEG/63.jpg"
htmlURL = "http://google.com"

savePath1="c:/test1.jpg"
savePath2="c:/index.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()

saveFile1 = open(savePath1, 'wb')
saveFile1.write(f)
saveFile1.close()

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)

print("다운로드 완료!")