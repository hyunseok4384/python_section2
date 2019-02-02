import pytube
import os
import subprocess


  #다운받을 동영상 URL 지정
yt = pytube.YouTube("https://www.youtube.com/watch?v=cS-IiArGmcU")
#https://www.youtube.com/watch?v=Q6_UJeJLt3E

videos = yt.streams.all()
print('videos', videos)

"""
for i in range(len(videos)):
    print(i, ',', videos[i])

cNum = int(input("다운 받은 화질은?"))

down_dir = r"c:\my_youtube"

videos[cNum].download(down_dir)

newFileName = input("변환 할 mp3이름은?")
oriFileName = videos[cNum].default_filename

subprocess.call(['ffmpeg', '-i',
    os.path.join(down_dir, oriFileName),
    os.path.join(down_dir, newFileName)
])

print("동영상 다운로드 및 mp3 변환 완료!")
"""
