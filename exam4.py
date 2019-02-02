from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base = "https://www.inflearn.com/"
quote = rep.quote_plus("추천-강좌")
url = base + quote
print(url)

res = req.urlopen(url)
SavePath = "c:\\exam\\"

try:
    if not (os.path.isdir(SavePath)):
        os.makedirs(SavePath)
except OSError as e:
    e.errno != errno.EEXIST
    print("폴더 만들기 실패!")
    raise

soup = BeautifulSoup(res, "html.parser")

All_list = soup.select("ul.slides")
q=1
for i in All_list:
    for e in i:
        with open(SavePath+"text_"+str(q)+".txt", "wt") as fp:
            fp.write(e.select_one("h4.block_title > a").string)
        FullFileName = os.path.join(SavePath+str(q)+".jpg")
        req.urlretrieve(e.select_one("div.block_media > a > img")['src'], FullFileName)
        q+=1
print("다운로드 완료!")
