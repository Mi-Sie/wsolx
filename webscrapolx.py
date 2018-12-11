from requests import get
from bs4 import BeautifulSoup as bs

##import links
subaruUrl = 'https://www.olx.pl/motoryzacja/samochody/subaru/forester/?search[filter_float_price:to]=40000&search[filter_float_year:from]=2002&search[filter_float_year:to]=2008&search[filter_float_enginepower:from]=200'
## site: olx

## get the link

urlContent = get(subaruUrl)
soup = BeautifulSoup.get()
print(urlContent.content)

## get the ad list
## get the link content
## store link content