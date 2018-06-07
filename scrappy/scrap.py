import requests
import bs4
import csv

# req = requests.get('https://learncodeonline.in')
# print(type(req))
# # print(req.text)
# soup = bs4.BeautifulSoup(req.text, 'lxml')
# print(type(soup))
# hi = soup.select('title')
# print(hi)
# print(hi[0])
# print(hi[0].getText())


# req = requests.get('https://en.wikipedia.org/wiki/Machine_learning')
# soup = bs4.BeautifulSoup(req.text, 'lxml')
# data = soup.select('.mw-headline')
# for i in data:
#     print(i.text)


# req = requests.get('https://en.wikipedia.org/wiki/Machine_learning')
# soup = bs4.BeautifulSoup(req.text, 'lxml')
# for i in soup.select('.toc > ul > li'):
#     print(i.text)


# print([i.text for i in soup.select('.toc > ul > li')])



req = requests.get('http://coreyms.com/').text
soup = bs4.BeautifulSoup(req, 'lxml')

csv_file = open('CMS_Scrap.csv','w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for artical in soup.find_all('article'):
    headline = artical.h2.a.text
    print(headline)
    summary = artical.find('div', class_='entry-content').p.text
    print(summary)
    try:
        vid_src = artical.find('iframe', class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)
    print()

    csv_writer.writerow([headline.encode("utf-8"),summary.encode("utf-8"),yt_link.encode("utf-8")])

csv_file.close()
