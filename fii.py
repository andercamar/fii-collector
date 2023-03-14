import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from datetime import date

class ticket:
    def __init__(self,ticket,value,dy,div,pvp,quotaValue):
        self.ticket = ticket
        self.value = value
        self.dy = dy
        self.div = div
        self.pvp = pvp
        self.quotaValue = quotaValue
        self.date = date.today()

def getValues(indicator):
    return float(indicator.find('b').text.replace(",","."))

def getData(fii):
    url = os.environ['url']
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get(url+fii,headers=headers)
    soup = BeautifulSoup(response.text,"html.parser")
    value = soup.find('div',class_="item quotation").find('span',class_="value").text
    indicators = soup.find_all('div',class_="indicators__box")
    dy = getValues(indicators[0])
    div = getValues(indicators[1])
    pvp = getValues(indicators[3])
    quotaValue = getValues(indicators[6])
    return ticket(fii,value,dy,div,pvp,quotaValue)

def getFundos():
    list = []
    fundos = ['mxrf11','snci11']
    for fundo in fundos:
        list.append(getData(fundo))
    for x in list:
        print(x.ticket)
        print(x.value)
        print(x.dy)
        print(x.div)
        print(x.pvp)
        print(x.quotaValue)
        print(x.date)

def main():
    load_dotenv()
    getFundos()

if __name__ == '__main__':
    main()