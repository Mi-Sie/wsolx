from requests import get
from bs4 import BeautifulSoup as bs

##import links
dataUrl = 'https://www.olx.pl/motoryzacja/samochody/subaru/forester/?search[filter_float_price:to]=40000&search[filter_float_year:from]=2002&search[filter_float_year:to]=2008&search[filter_float_enginepower:from]=200'
## site: olx

## get the data
urlContent = get(dataUrl).content
##text


## get the ad links
##<td class="offer  ">
contentSoup = bs(urlContent, 'html.parser')
print(contentSoup)



## get the link content
## store link content