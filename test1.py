import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgURL="http://blogfiles.naver.net/20120923_166/ahnsuyeon920_134840415691074Fw5_JPEG/63.jpg"

saveP1="c:/test11.jpg"

ff=dw.urlopen(imgURL).read()

with open(saveP1,"wb") as fd:
    fd.write(ff)

print("성공했습니다!")
