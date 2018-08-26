from bs4 import BeautifulSoup
import requests

src = requests.get('http://coreyms.com').text

soup = BeautifulSoup(src, 'lxml')

#  article = soup.find('article')

for article in soup.findall('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        video_src = article.find('iframe', class_='youtube-player')['src']
        video_id = video_src.split('/')[4]
        video_id = video_id.split('?')[0]
        youtube_link = f"https://www.youtube.com/watch?v={video_id}"
    except Exception as e:
        raise e
    print(youtube_link)

    print()
