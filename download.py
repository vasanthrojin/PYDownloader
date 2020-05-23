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
prev_list = os.listdir()
streams.filter(only_video=True, resolution=quality_choice).first().download()
streams.filter(only_audio=True).first().download('audio')
fileIt = 'Youtube'
for file in os.listdir():
    if file not in prev_list:
        fileIt = file
os.system("ffmpeg -i '"+os.getcwd()+'/'+fileIt+"' -i "+os.getcwd()+"'/audio/"+fileIt+"' -c:v copy -c:a aac output.mp4")
print('Done dana done!')
os.remove(fileIt)
os.remove('audio/'+fileIt)
os.rename(r'output.mp4', fileIt)
