from requests import get
from bs4 import BeautifulSoup as bs

##import links
#TODO store links
dataUrl = 'https://www.olx.pl/motoryzacja/samochody/subaru/forester/?search[filter_float_price:to]=40000&search[filter_float_year:from]=2002&search[filter_float_year:to]=2008&search[filter_float_enginepower:from]=200'


## get the data
#TODO if respone <> 200
urlContent = get(dataUrl).content

## get the ad links
##<td class="offer  ">
contentSoup = bs(urlContent, 'html.parser')


td = contentSoup.find_all('tr', class_ = 'wrap')

print(len(td))
## get the link content

## store link content