import urllib.request as req
url = "https://www.ptt.cc/bbs/Baseball/index.html"
request = req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
# print(data)
import bs4
root = bs4.BeautifulSoup(data, 'html.parser')
titles = root.find_all('div', class_='title')
for title in titles:
    if title.a != None:
        print(title.a.string)