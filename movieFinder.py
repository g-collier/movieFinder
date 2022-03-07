import re
from bs4 import BeautifulSoup
import urllib3
import time




#selecting the URL we want to scrape from
url = 'https://www.imdb.com/feature/genre/?ref_=kw_brw_1'

ourURL = urllib3.PoolManager().request('GET', url).data

#getting/parsing the html
soup = BeautifulSoup(ourURL, 'lxml')

#Getting User Description for the movie they want


movieList = []
userGenre = input("What genre of movie do you want to see? ") 

movieYear = input("List the earliest year you're willing to watch (i.e 1984): ")

movieRating = input("What's the lowest rating you're willing to endure? (i.e 1-5 star): ") 











mydivs = soup.find_all('div', {'class': 'table-cell primary'})

for i in mydivs:
        for e in i:
                for x in e:
                        if(x not in movieList):
                                movieList.append(x)
                        elif(x in movieList):
                                pass
                        

print(movieList)
                                
                        






     
     
     
     
     
     
     
     
     




#filter by genre (use different URL's based on user answer)

#filter by year (can be done with BeautifulSoup and conditionals)

#filter by rating (same as above)

#summary: we're going to ask the user for their input on what they want to watch (genre, rating, year, etc.). We'll then filter these results using individual URLs with beautiful soup.

#There's got to be a different way of selecting the genre's without manually inputting each genre.

#we can try to search for the a href's 
