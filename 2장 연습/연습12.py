Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests

url = 'http://bit.ly/2JnsHnT'
r = requests.get(url, stream = True).raw

from PIL import Image

img = Image.open(r)
img.show()
img.save('src.png')

