import requests as r, bs4

#Calculates the last page number in the website 'https://www.hdwallpapers.in'
def calcLastpage(url):
	# WallReq stores the complete html response of the 'https://www.hdwallpapers.in'
	wallReq= r.get(url, verify=False)
	# WallSoup parses the wallReq html content
	wallSoup= bs4.BeautifulSoup(wallReq.text, "lxml")
	#The link to the last page number lies in <a> html tag under class pagination, So selecting that part in from WallSoup
	lastPage=wallSoup.select('.pagination a')
	if lastPage == []:
		lastno=1
	else:
		# Structure of the page's source tells us that the last no is inside second last a tag
		lastno=lastPage[-2].string
	return lastno
