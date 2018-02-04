from bs4 import BeautifulSoup as soup 
from urllib2 import urlopen


url="https://www.bloombergquint.com/stock/901145/indian-oil-corp"

client=urlopen(url)
html_page=client.read()
client.close()

page=soup(html_page,"html.parser")
html_page2=page.findAll("div",{"class":"widget-content"})[0]
chart_link= html_page2.iframe['data-src']
client2=urlopen(chart_link)
html_page3=client2.read()
client2.close()
page2=soup(html_page3,"html.parser")

x1=page2.findAll("div",{"class":"bbcard"})[0]
x2=x1.div.div
x3=x2.findAll("div",{"class":"main-price-graph"})[0]
print x3