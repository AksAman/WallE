# WallE
A python web scraping project which automatically downloads a random and sets it on your desktop depending upon a few inputs.

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
- main.py
  
  
# Python package dependencies

- requests
- BeautifulSoup4

Run `sudo pip -r requirements.txt` from your terminal to install the dependencies
