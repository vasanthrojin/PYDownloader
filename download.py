from pytube import YouTube
from youtube_search import YoutubeSearch
import os

print("Download Youtube videos 😃!")
search = str(input('Enter song name: '))
results = eval(YoutubeSearch(search, max_results=10).to_json())
count = 0
for result in results['videos']:
    print(count+1, '.'+' '+str(results['videos'][count]['title']))
    count += 1
choice = int(input('Please choose your video title: '))
link = results['videos'][choice-1]['link']
streams = YouTube("https://www.youtube.com"+link).streams
quality = []
for streame in streams:
    if streame.resolution not in quality:
        quality.append(streame.resolution)
quality = sorted([i for i in quality if i])
print()
print('Please choose you video quality:')
count = 0
for res in quality:
    print(count+1, '. ', res)
    count += 1
quality_choice = quality[int(input('Choice: '))-1]
print('Downloading ...')

cdw = os.getcwd()
os. chdir("outputs/audio/")
cdo = os.getcwd()
prev_list = os.listdir()
os.chdir(cdw)

streams.filter(only_video=True, resolution=quality_choice).first().download("outputs/video")
streams.filter(only_audio=True).first().download('outputs/audio')
fileIt = 'Youtube'


os. chdir(cdo)


for file in os.listdir():
    if file not in prev_list:
        fileIt = file

os. chdir(cdw+"/outputs")
print('Merging video and audio .....')
combine = 'ffmpeg -i "'+os.getcwd()+'/video/'+fileIt+'" -i "'+os.getcwd()+'/audio/'+fileIt +'"'+ " -c:v copy -c:a aac output.mp4"

os.system(combine)
print('video and audio Merging complete')
print("\n deleting temporary files")

os.remove("video/"+fileIt)
os.remove('audio/'+fileIt)
os.rename(r'output.mp4', fileIt)
print("deletion complete")