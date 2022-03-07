from bs4 import BeautifulSoup
import urllib3
import random
"""
This pageFinder function is used to determine which genre page actually ends up getting scraped based on user input/random number generator. 
I was originally going to try to write a couple for loops and append the titles of the top 50 films into a list, and print it out that way; 
but it ended up getting a little convoluted when I decided to add multiple pages as I would of had to have 24 lists with 50 movies in each list.
It seemed more efficient to just hard code the 24 genre pages. I also made note to write this disgusting long function in another document because
I didn't want to drop this behemoth in main and work around it.

"""
def pageFinder(x):
        if x == "action" or x == "1":
                url = 'https://www.imdb.com/search/title/?genres=action&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=R1ZF5MXQ8GX6B5YRN8X4&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_1'
                ourURL = urllib3.PoolManager().request('GET', url).data
                soup = BeautifulSoup(ourURL, 'html.parser')
                return soup
        elif x == "adventure" or x == "2":
                url = 'https://www.imdb.com/search/title/?genres=adventure&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=CWKFMQPSJ1C4T6H00XJB&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_2'
                ourURL = urllib3.PoolManager().request('GET', url).data
                soup = BeautifulSoup(ourURL, 'html.parser')
                return soup
        elif x == "animation" or x == "3":
                url = 'https://www.imdb.com/search/title/?genres=animation&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=CWKFMQPSJ1C4T6H00XJB&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_3'
                ourURL = urllib3.PoolManager().request('GET', url).data
                soup = BeautifulSoup(ourURL, 'html.parser')
                return soup
        elif x == "biography" or x == "4":
                url = 'https://www.imdb.com/search/title/?genres=biography&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=Y5YX320KDVT73VABTCCV&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_4'
                ourURL = urllib3.PoolManager().request('GET', url).data
                soup = BeautifulSoup(ourURL, 'html.parser')
                return soup
        elif x == "comedy" or x == "5":
                url = 'https://www.imdb.com/search/title/?genres=comedy&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=AW7ED2SXVHAWKDT60MNK&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_5'
                ourURL = urllib3.PoolManager().request('GET', url).data
                soup = BeautifulSoup(ourURL, 'html.parser')
                return soup
        elif x == "crime" or x == "6":
                url = 'https://www.imdb.com/search/title/?genres=crime&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=HKQ0PBSFFMSM8XF594PD&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_6'
                ourURL = urllib3.PoolManager().request('GET', url).data
                soup = BeautifulSoup(ourURL, 'html.parser')
                return soup
        elif x == "documentary" or x == "7":
                url = 'https://www.imdb.com/search/title/?genres=documentary&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=BPB5MPCPNB85VV5858PN&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_7'
                ourURL = urllib3.PoolManager().request('GET', url).data
                soup = BeautifulSoup(ourURL, 'html.parser')
                return soup
        elif x == "drama" or x == "8":
                url = 'https://www.imdb.com/search/title/?genres=drama&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=RWNB5YWV9BQDTRW8RW22&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_8'
                ourURL = urllib3.PoolManager().request('GET', url).data
                soup = BeautifulSoup(ourURL, 'html.parser')
                return soup
        elif x == "family" or x == "9":
                url = 'https://www.imdb.com/search/title/?genres=family&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=ZV07WJVZSWX2QEZTD1M9&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_9'
                ourURL = urllib3.PoolManager().request('GET', url).data
                soup = BeautifulSoup(ourURL, 'html.parser')
                return soup
        elif x == "fantasy" or x == "10":
                url = 'https://www.imdb.com/search/title/?genres=fantasy&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=JWWNQDH053KPEW29BJWT&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_10'
                ourURL = urllib3.PoolManager().request('GET', url).data
                soup = BeautifulSoup(ourURL, 'html.parser')
                return soup
        elif x == "film-noir" or x == "film noir" or x == "11":
                url = 'https://www.imdb.com/search/title/?genres=film-noir&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=0AS65GH85F4M15P05TE5&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_11'
                ourURL = urllib3.PoolManager().request('GET', url).data
                soup = BeautifulSoup(ourURL, 'html.parser')
                return soup
        elif x == "history" or x == "12":
                url = 'https://www.imdb.com/search/title/?genres=history&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=3R4MJ3G0HGD4AK8MVKMV&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_12'
                ourURL = urllib3.PoolManager().request('GET', url).data
                soup = BeautifulSoup(ourURL, 'html.parser')
                return soup
        elif x == 'horror' or x == "13":
                url = 'https://www.imdb.com/search/title/?genres=horror&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=9W3KDVNCHCYT70XW2P0E&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_13'
                ourURL = urllib3.PoolManager().request('GET', url).data
                soup = BeautifulSoup(ourURL, 'html.parser')
                return soup
        elif x == 'music' or x == "14":
                url = 'https://www.imdb.com/search/title/?genres=music&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=7ZJKPHBWBDT82F9BYA3T&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_14'
                ourURL = urllib3.PoolManager().request('GET', url).data
                soup = BeautifulSoup(ourURL, 'html.parser')
                return soup
        elif x == 'musical' or x == "15":
                url = 'https://www.imdb.com/search/title/?genres=musical&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=JA9H5KCHS2BZEK78EVFY&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_15'
                ourURL = urllib3.PoolManager().request('GET', url).data
                soup = BeautifulSoup(ourURL, 'html.parser')
                return soup
        elif x == 'mystery' or x == "16":
                url = 'https://www.imdb.com/search/title/?genres=mystery&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=JA9H5KCHS2BZEK78EVFY&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_16'
                ourURL = urllib3.PoolManager().request('GET', url).data
                soup = BeautifulSoup(ourURL, 'html.parser')
                return soup
        elif x == 'romance' or x == "17":
                url = 'https://www.imdb.com/search/title/?genres=romance&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=JA9H5KCHS2BZEK78EVFY&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_17'
                ourURL = urllib3.PoolManager().request('GET', url).data
                soup = BeautifulSoup(ourURL, 'html.parser')
                return soup
        elif x == 'sci-fi' or x == "18":
                url = 'https://www.imdb.com/search/title/?genres=sci-fi&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=JA9H5KCHS2BZEK78EVFY&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_18'
                ourURL = urllib3.PoolManager().request('GET', url).data
                soup = BeautifulSoup(ourURL, 'html.parser')
                return soup
        elif x == 'short film' or x == "19":
                url = 'https://www.imdb.com/search/title/?genres=short&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=JA9H5KCHS2BZEK78EVFY&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_19'
                ourURL = urllib3.PoolManager().request('GET', url).data
                soup = BeautifulSoup(ourURL, 'html.parser')
                return soup
        elif x == 'sport' or x == "sports" or x == "20":
               url = 'https://www.imdb.com/search/title/?genres=sport&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=JA9H5KCHS2BZEK78EVFY&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_20'
               ourURL = urllib3.PoolManager().request('GET', url).data
               soup = BeautifulSoup(ourURL, 'html.parser')
               return soup
        elif x == 'superhero' or x == "21":
                url = 'https://www.imdb.com/search/keyword/?keywords=superhero&title_type=movie&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=JA9H5KCHS2BZEK78EVFY&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_21'
                ourURL = urllib3.PoolManager().request('GET', url).data
                soup = BeautifulSoup(ourURL, 'html.parser')
                return soup
        elif x == 'thriller' or x == "22":
                url = 'https://www.imdb.com/search/title/?genres=thriller&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=JA9H5KCHS2BZEK78EVFY&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_22'
                ourURL = urllib3.PoolManager().request('GET', url).data
                soup = BeautifulSoup(ourURL, 'html.parser')
                return soup
        elif x == 'war' or x == "23":
                url = 'https://www.imdb.com/search/title/?genres=war&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=JA9H5KCHS2BZEK78EVFY&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_23'
                ourURL = urllib3.PoolManager().request('GET', url).data
                soup = BeautifulSoup(ourURL, 'html.parser')
                return soup
        elif x == 'western' or x == "24":
                url = 'https://www.imdb.com/search/title/?genres=western&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=JA9H5KCHS2BZEK78EVFY&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_24'
                ourURL = urllib3.PoolManager().request('GET', url).data
                soup = BeautifulSoup(ourURL, 'html.parser')
                return soup
        else:
                print("I'm sorry, there was no genre matching your criteria.")
                