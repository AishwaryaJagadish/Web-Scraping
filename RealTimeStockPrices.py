from bs4 import BeautifulSoup
import requests

#change the url as you need for whichever company needed
url = 'https://finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch'


#soup -  gets the whole html of the page
def ParsePrice():
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    price= soup.find('fin-streamer', class_="Fw(b) Fz(36px) Mb(-4px) D(ib)").text
    return price

while True:
    print('Stock Current Price is: '+str(ParsePrice()))