from bs4 import BeautifulSoup

def getContent(file):
	return open(file, "r").read()

def getShortlist(content):
	soup = BeautifulSoup(content, features="html.parser")
	shortlist = []

	for tr in soup.findAll("tr", {"class" : "isFav"}):
		info = tr.findAll("td")
		listing = ""

		listing += info[2].text + " - "

		listing += info[3].findAll("span")[-1].text.strip()

		if info[8].text == "":
			listing += "\n\t\t " + "Unknown" + " - "
		else:
			listing += "\n\t\t " + info[8].text + " - "

		listing += info[6].text + " : " + info[10].text + "\n"

		shortlist.append(listing)

	return shortlist

html = "University of Waterloo - MyAccount - Hire Waterloo Co-op - Jobs _ Applications.html"

content = getContent(html)
file = open("shortlist.txt", "w")

for listing in getShortlist(content):
	file.write(listing + "\n")