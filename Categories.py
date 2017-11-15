import requests as r, bs4, random


#Gets the wallpaper categories from the url 
def getCategories(url):
	# Getting the complete page as a response object in variable catPage
	catPage= r.get(url, verify=False)
	catSoup= bs4.BeautifulSoup(catPage.text, "lxml")
	
	# The categories are stored as links inside the 'li' tag under class 'categories'
	# Parsing the categories as list and storing in cat
	cat=catSoup.select('.categories li a')
	
	# Making a dictionary 'catDict' with key as the Category and value as the link to the category page
	# c refers to each entry in the catDict
	catDict={c.string:mainUrl+c.get('href') for c in cat}
	
	# 'i' is the counter to display each category
	i=1
	
	for k,v in catDict.items():
		# Printing all the categories as '1. category_1'
		print(str(i)+'. '+k)
		i=i+1
	
	print('Choose Category (enter the index) : ')
	
	# The python dictionaries are unordered and thus have no indexing.
	# So, if we want to choose category using just the index
	# Convert dictionary to a temporary list 'catList' 
	catList=list(catDict)
	
	# Taking the index as input
	index=int(input())
	
	# The target page's url will be the 'catDict' value corresponding to the key as the 'catList' value at position 'index-1'
	# Storing the url of the target category page in 'page'
	catPage=catDict[catList[index-1]]
	
	return catPage
