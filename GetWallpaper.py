import requests as r, bs4,random
from urls import mainUrl, file_url
from LastPageCalculator import calcLastpage
from SetWallpaper import setter
from Image_downloader import imageDownloader


# Function to get the wallpaper
# 'choice' decides whether any random wallpaper should be set or a random wallpaper from a chosen category
def getter(url,choice):
	
	# Calling calcLastpage() and storing last page number as 'lastPage'
	lastPage = int(calcLastpage(url))
	# Choosing a random page number ranging from 1 to the last page no
	randpage_no = random.randint(1,lastPage)
	
	# deciding url on the basis of user's choice
	if choice is 1:
		url='https://www.hdwallpapers.in/latest_wallpapers/page/'
	else:
		url=f_url[-5]+'/page/'
	
	#Targetpage's url	
	pageTarget  =url+str(randpage_no)
	
	# getting Target page as response object 'pageR'
	pageR=r.get(pageTarget, verify=False)
	
	# Parsing targetPage as 'pageSoup'
	pageSoup= bs4.BeautifulSoup(pageR.text, "lxml")
	
	# Storing all the image links on the page in 'links'
	# the links are under class 'thumb' under 'div' tag
	links=pageSoup.select('div .thumb a')
	
	# extracting the links from 'links' and appending in 'listLink'
	listLink=[]
	for link in links:
	  listLink.append(mainUrl+link.get('href'))
	
	# Choosing a random wallpaper link from the 'listLink'
	randImageIndex = random.randint(1,(len(listLink)-1))
	imgUrl=listLink[randImageIndex]
	
	#Getting Image url page as response object
	imageR = r.get(imgUrl, verify=False)
	imageS = bs4.BeautifulSoup(imageR.text, "lxml")
	
	# Wallpaper page contains a lot of resolutions under class 'wallpaper-resolutions' , 
	# but the link with target='_blank' contains resolution with name as 'original' which is common in all wallpapers
	imgTag=imageS.select('.wallpaper-resolutions a[target="_blank"]')
	
	#Checking if image is not found
	if imgTag==[]:
		print('image not found')
		
	# Getting the image Url
	imageUrl=mainUrl+(imgTag[0].get('href'))
	#saving the image
	imageDownloader(imageUrl)
	setter(file_url, imageUrl)
	return imageUrl
