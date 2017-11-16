# WallE
A python web scraping project which automatically downloads a random wallpaper and sets it on your desktop depending upon a few inputs.

# Project Description
I made this project in order to learn web scraping. I have used requests and beautiful soup 4 to scrap a webpage and download wallpapers from there. When you run the `main.py`, you have two choices - set any random wallpaper or choose a category and then set the random wallpaper from that category.

# How to run this project?
* Open your terminal and enter `python main.py`, if you have only python=>3 installed, else use `python3 main.py`
* You will be asked for either entering 1 or 2.
* If you choose 1
  - The program will download a random wallpaper and set it as your destop wallpaper
* If you choose 2
  - You will be first asked to choose a category. Enter the index accordingly and WallE will set your desktop wallpaper.
  
# What different files do?
Basically, i have broken my entire project into different modules. Let's go by them one by one:
- [`main.py`](https://github.com/AksAman/WallE/blob/master/main.py)
  The main python file which calls other functions from different modules. You just need to run this one and chill.
  
- [`urls.py`](https://github.com/AksAman/WallE/blob/master/urls.py)
  * mainUrl: The main url of the website,as i have used the main url of the website again and again.
  * file_url: The file path where the wallpaper gets stored. By default, images gets stored in 'wallpapers' folder in the project's directory. You can change it by changing variable `dirName`. I have used `os.system`, because it will make WallE adjust file namings depending on the os you are using.
  
- [`Image_downloader.py`](https://github.com/AksAman/WallE/blob/master/Image_downloader.py)
  Downloads the wallpaper using the given 'image url' and saves in `dirName`
  
- [`LastPageCalculator.py`](https://github.com/AksAman/WallE/blob/master/LastPageCalculator.py)
  As i am using random wallpapers, so i am using 
  [`random.randint()`](https://docs.python.org/3/library/random.html#random.randint) python function. As it needs an upper bound, i am using `calcLastpage()` which find the last page for the website.
  
- [`Categories.py`](https://github.com/AksAman/WallE/blob/master/Categories.py)
It scraps the categories of wallpapers and returns the url of the chosen category's page.

- [`SetWallPaper.py`](https://github.com/AksAman/WallE/blob/master/SetWallpaper.py)
It uses the gnome command `gsettings set org.gnome.desktop.background picture-uri fileurl` to set the wallpaper from the directory specified.

- [`GetWallpaper.py`](https://github.com/AksAman/WallE/blob/master/GetWallpaper.py)
The heart of the project which uses 'image downloader', 'SetWallpaper' modules to parse the main pages, get the image links, select a random image, download it, save it, and finally set the wallpaper.
  
  
# Python package dependencies

- requests
- BeautifulSoup4

Run `sudo pip install -r requirements.txt` from your terminal to install the dependencies
