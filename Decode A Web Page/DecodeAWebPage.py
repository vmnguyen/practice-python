#!/usr/bin/python3
#Author: bob
from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.nytimes.com/')
result = r.text
soup = BeautifulSoup(result, 'html.parser')
for i in soup.find_all(class_="story-heading"):
	if i.a:
		print (i.a.text.replace("\n", " ").strip())
	else:
		print (i.text.strip())