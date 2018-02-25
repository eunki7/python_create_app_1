import os
import subprocess

import pytube

yt = pytube.YouTube("https://www.youtube.com/watch?v=WH7xsW5Os10") #다운받을 동영상 URL 지정

vids= yt.streams.all()

#영상 형식 리스트 확인
for i in range(len(vids)):
    print(i,'. ',vids[i])

vnum = int(input("다운 받을 화질은? "))

parent_dir = "C:\section2\download"
vids[vnum].download(parent_dir) #다운로드 수행

new_filename = input("변환 할 mp3 파일명은?")

default_filename = vids[vnum].default_filename 
subprocess.call(['ffmpeg', '-i',                 #cmd 명령어 수행
    os.path.join(parent_dir, default_filename),
    os.path.join(parent_dir, new_filename)
])

print('동영상 다운로드 및 mp3 변환 완료!')
