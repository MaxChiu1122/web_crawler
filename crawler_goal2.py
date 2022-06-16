import urllib.request as req
url = "https://tw.stock.yahoo.com/rank/price"
request = req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
#print(data)
import bs4
root = bs4.BeautifulSoup(data, 'html.parser')
titles = root.find_all('div', class_='Lh(20px) Fw(600) Fz(16px) Ell')
prices_up = root.find_all('span', class_='Jc(fe) Fw(600) D(f) Ai(c) C($c-trend-up)')
prices_down = root.find_all('span', class_='Jc(fe) Fw(600) D(f) Ai(c) C($c-trend-down)')
prices = root.find_all('span', class_='Jc(fe) Fw(600) D(f) Ai(c)')
t = []
p = []
for title in titles:
    if title.string != None:
        t.append(title.string)
for price in prices_up:
    if price.string != None:
        p.append(float(price.string.replace(',', '')))
for price in prices_down:
    if price.string != None:
        p.append(float(price.string.replace(',', '')))
for price in prices:
    if price.string != None:
        p.append(float(price.string.replace(',', '')))
price = sorted(p, reverse = True)
price_str = [str(x) for x in price]
list_combined = [x[0] + ', ' + x[1] for x in list(zip(t, price_str))]
print(list_combined)