#! python3
# multithreadXKCD.py - Downloads every single XKCD comic.

import requests, os, bs4, threading
os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd


def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page
        print("Downloading page http://xkcd.com/%s..." % (urlNumber))
        res = requests.get("http://xkcd.com/%s" % (urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)

        # Find the URL of image
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print("Could not find image.")
        else:
            comicUrl = comicElem[0].get('src')
            print("Downloading image %s..." % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()

            imageFile = open(
                os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(1000000):
                imageFile.write(chunk)
            imageFile.close()


downloadThreads = []
for i in range(0, 1400, 100):  # 14 threads
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end
for downloadThread in downloadThreads:
    downloadThread.join()
print("Done.")
