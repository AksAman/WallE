import os

def setter(file_url, imageUrl):
	#Command in linux to set wallpaper
	linuxCommand = 'gsettings set org.gnome.desktop.background picture-uri '
	
	#Destination where wallpaper has to be stored
	destination = file_url
	imgName = imageUrl[34:].strip('_')
	os.system(linuxCommand+file_url+'/'+imgName)
	print('Wallpaper changed and new wallpaper is '+imgName)
