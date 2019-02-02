import sys
import io
import urllib.request as req

url="https://ssl.pstatic.net/tveta/libs/1222/1222734/0d21dc49f9e72ace4fc4_20190103102302796.jpg"
saveName="c:/exma1.jpg"

mpurl="https://tvetamovie.pstatic.net/libs/1222/1222371/90b762902e23a1269e9e_20190102150828016.mp4-pBASE-v0-f71383-20190102150925792.mp4"
saveName2="c:/exam2.mp4"


img = req.urlretrieve(url, saveName)
print("success!")

mp4=req.urlretrieve(mpurl, saveName2)
print("success2!")

#sub_pack > div.z_aside.section.rktshp > div.realtime_srch > ol
#ac_banner_a > img
#da_brand > div > a > video
