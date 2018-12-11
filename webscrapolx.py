from requests import get
from bs4 import BeautifulSoup as bs

##import links
dataUrl = 'https://www.olx.pl/motoryzacja/samochody/subaru/forester/?search[filter_float_price:to]=40000&search[filter_float_year:from]=2002&search[filter_float_year:to]=2008&search[filter_float_enginepower:from]=200'
## site: olx

## get the link

urlContent = get(dataUrl).text
##text


print(type(urlContent))


print(urlContent)




## get the ad list
##<td class="offer  ">
soup = bs.find_all(urlContent)
## get the link content
## store link content