from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL :- ")
html = urllib.request.urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
