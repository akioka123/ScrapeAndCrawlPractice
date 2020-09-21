import requests
from bs4 import BeautifulSoup

url = "http://travisbouldering.com/news/"

response = requests.get(url)
response.encoding = response.apparent_encoding
bs = BeautifulSoup(response.text, "lxml")
main = bs.find_all("dt")
for one in main:
    string = str(one.string)
    mess = string.split()
    print(mess[0])
