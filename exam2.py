import pytube
import os
import subprocess

ans=int(input("동영상 몇개를 받을래? "))
down_dir = r"c:\my_youtube"

if ans > 0 :
    for i in range(0,ans) :
        urlList=""
        print(i+1,"번째 동영상 작업 시작!")
        urlList = input("URL을 입력 하세요 : ")
        yt = pytube.YouTube(urlList)
        yt_list = yt.streams.all()

        for j in range(len(yt_list)) :
            print(j, " , ", yt_list[j])

        c_num = int(input("다운받을 화질은? "))
        yt_list[c_num].download(down_dir)
        ans = input("mp3로 변환할래? ")
        if ans == "y" or ans == "Y" :
            NewFileName = input("mp3로 저징할 파일이름을 입력하세요 :")
            OldFileName = yt_list[c_num].default_filename
            subprocess.call(['ffmpeg', '-i',
                os.path.join(down_dir, OldFileName),
                os.path.join(down_dir, NewFileName)
            ])
        elif ans == "n" or ans == "N":
            print("No를 선택했습니당")
            pass
        else :
            print("잘못된 입력값입니다")
            os._exit()
else :
    print("0이상의 숫자를 입력하세요")
    os._exit()
