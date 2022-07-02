from pytube import YouTube
import time
import os
print("Welcome to Metric Youtube Downloader!")
time.sleep(2)
downloads =int( input("How many items do you want to download? "))
n = 0
while n < downloads:  
	print("Please enter your YouTube Link Down Below")
	link = input("Enter the link: ")
	yt = YouTube(link)
	n  +=  1
	time.sleep(2)
	print("Your Youtube Video: ", yt.title)
	time.sleep(1)
	print("Video Length: ",yt.length)
	time.sleep(1)
	type =int(input("Do you want to download Audio or Video:\n- Reply With 1 for Audio or\n -2 for Video: "))


	if type == 2 :
		yt.streams.filter(only_video=True)
		highest_quality = yt.streams.get_highest_resolution()
		new_name =input("Enter your File name: \n")
		print("The Video is being downloaded in this directory")
		highest_quality.download(filename=new_name)
		time.sleep(3)
		print("Downloading...")


	elif type == 1 :
		destination = '.'
		audio = yt.streams.filter(only_audio=True).first()
		new_name =input("Enter your File name: \n")
		out_file = audio.download(output_path=destination,filename=new_name)
		# save the file
		base, ext = os.path.splitext(out_file)
		new_file = base + '.mp3'
		os.rename(out_file, new_file)
		print("Your Audio file is being downloaded!")
		time.sleep(2)
		print("Downloading...")
		time.sleep(2)
		print("Downloaded")


	else:
		print("Enter the speccified Input!")




