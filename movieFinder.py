import re
from bs4 import BeautifulSoup
import urllib3
import time


# Getting genre preference from the user
userGenre = input("What genre of movie do you want to see? ")

#method to set the genre URL without cluttering main


url = 'https://www.imdb.com/search/title/?genres=action&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=R1ZF5MXQ8GX6B5YRN8X4&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_1'

ourURL = urllib3.PoolManager().request('GET', url).data

soup = BeautifulSoup(ourURL, 'html.parser')

i = 1
movieList = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})

for div_item in movieList:

    div = div_item.find('div', attrs={'class':'lister-item-content'})
    print(str(i) + '.'),

    header = div.findChildren('h3', attrs={'class':'lister-item-header'})

    print('Movie: ' + str((header[0].findChildren('a'))[0].contents[0].encode('utf-8').decode('ascii', 'ignore')))

    i += 1






#might have to go link by link














