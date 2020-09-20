from bs4 import BeautifulSoup

def getContent(file):
	return open(file, "r").read()

def getShortlist(content):
	soup = BeautifulSoup(content, features="html.parser")
	shortlist = []

	for tr in soup.findAll("tr", {"class" : "isFav"}):
		jobID = tr.findAll("td")[2].text
		shortlist.append(jobID)

	return shortlist

html = "University of Waterloo - MyAccount - Hire Waterloo Co-op - Jobs _ Applications.html"
file = open("shortlist.txt", "w")

for jobID in getShortlist(getContent(html)):
	file.write(jobID + "\n")