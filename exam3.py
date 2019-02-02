from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.daum.net/"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")

recommand = soup.select("div.hotissue_builtin.hide > div.realtime_part > ol > li")

for i,e in enumerate(recommand,1):
    href=e.find("a").attrs['href']
    txt=e.find("a").string
    print(i,"위 : ", txt, "링크 : ", href)

#ol > li.current > div > div:nth-child(1) > span.txt_issue > a
