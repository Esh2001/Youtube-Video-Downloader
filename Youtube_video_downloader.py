from pytube import YouTube

link = input("Enter the link you want to download: ")
yt = YouTube(link)
print("Title: ",yt.title)
print("View: ",yt.views)
yd = yt.streams.get_highest_resolution()
yd.download('Downloads')