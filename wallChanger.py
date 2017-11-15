from GetWallpaper import getter
from urls import mainUrl
from Categories import getCategories

print('1. Do you want any random wallpaper')
print('2. You want to choose by category')
choice=int(input())
while choice is not 1 and choice is not 2:
	print('Enter 1 or 2:')
	choice=int(input())
if choice is 1:
	getter(mainUrl,1)
elif choice is 2:
	catUrl=getCategories(mainUrl)
	print(catUrl)
	getter(catUrl,2)
