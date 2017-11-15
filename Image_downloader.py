import requests as r, os
from urls import dirName
#Function to download an image and save to the computer using an image url
def imageDownloader(imageUrl):
	#getting response object in variable res
	res = r.get(imageUrl, verify=False)
	
	#making a directory to save images
	if(not os.path.isdir(dirName)):
		os.system('mkdir '+dirName)
	
	#opening file in binary mode
	imageFile = open(os.path.join(dirName, os.path.basename(imageUrl)), 'wb')
	for chunk in res.iter_content(100000):
  		imageFile.write(chunk)
  	
	imageFile.close()
	print('Image downloaded')
