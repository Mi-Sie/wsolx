from requests import get
from bs4 import BeautifulSoup as bs

# get the links
#TODO store links in json with some additional data for future referrence
dataUrl = 'https://www.olx.pl/motoryzacja/samochody/subaru/forester/?search[filter_float_price:to]=40000&search[filter_float_year:from]=2002&search[filter_float_year:to]=2008&search[filter_float_enginepower:from]=200'

# get the data
#TODO connection error handler
# accept resp 200 only, log everything else (error status, id, name)
#TODO if file exist use flat file, if no get it from site
urlContent = get(dataUrl).content

# soupify the data
contentSoup = bs(urlContent, 'html.parser')

# get the ad containers
td = contentSoup.find_all('tr', class_='wrap')

print(type(contentSoup))
print(type(td))

# td2 = td.find_all('a')
# for i in td2:
#     print(i['href'])

## get the link content

## store link content