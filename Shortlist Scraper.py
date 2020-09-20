from bs4 import BeautifulSoup
import os
import sys

def getContent(file):
	return open(file, "r").read()

def getShortlist(content):
	soup = BeautifulSoup(content, features="html.parser")
	shortlist = []

	for tr in soup.findAll("tr", {"class" : "isFav"}):
		info = tr.findAll("td")
		listing = ""

		listing += info[2].text
		shortlist.append(listing)

	return shortlist

html = os.path.join(sys.path[0], "shortlist.html")

content = getContent(html)
file = open("shortlist.txt", "w")

for listing in getShortlist(content):
	file.write(listing + " ")