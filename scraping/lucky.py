#! usr/bin/env python3
# lucky.py - Opens several Google search results

# Here are the imports!
import requests, sys, webbrowser, bs4

print("Googling...")  # Display text while downloading the page

# Requests OBJ = google search ARGs in the command line
res = requests.get('http://google.com/search?q=' + " ".join(sys.argv[1:]))
# Check if there are errors
res.raise_for_status()

# Get top search results...
soup = bs4.BeautifulSoup(res.text)

# Open browser tab for each result
# class r, that is a link; store in a List
linkElems = soup.select('.r a')
# Open a maximum of 5 links
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
