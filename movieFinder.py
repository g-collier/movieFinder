import re
from bs4 import BeautifulSoup
import urllib3
from random import choice, randint
from theLinks import pageFinder


randNum1 = randint(1,24)
print(randNum1)
# Getting genre preference from the user
genrePicker = input("What genre would you like? You can also type random for a random genre ")
if genrePicker == 'random':
        genrePicker = str(randNum1)
               
print("\n")
userSelection = input("Would you like a random movie, or the top 50 from your selection? ")
                 
if userSelection.lower() == "top 50" or userSelection == "top" or userSelection == "50":
        print("\n")
        print("\n")
        
        i = 1
        movieList = pageFinder(genrePicker.lower()).findAll('div', attrs={'class': 'lister-item mode-advanced'})
        for div_item in movieList:
                div = div_item.find('div', attrs={'class':'lister-item-content'})
                print(str(i) + '.'),
                
                header = div.findChildren('h3', attrs={'class':'lister-item-header'})
                print('Movie: ' + str((header[0].findChildren('a'))[0].contents[0].encode('utf-8').decode('ascii', 'ignore')))
                
                i += 1
                                 
elif userSelection.lower() == "random" or userSelection.lower() == "random movie":
        print("\n")
        print("\n")
        
        movieList = pageFinder(genrePicker.lower()).findAll('div', attrs={'class': 'lister-item mode-advanced'})
        randMovie = choice(movieList)
        
        div = randMovie.find('div', attrs={'class':'lister-item-content'})
        header = div.findChildren('h3', attrs={'class':'lister-item-header'})
        print('Your random movie is called: '  + str((header[0].findChildren('a'))[0].contents[0].encode('utf-8').decode('ascii', 'ignore')))
        
        print("\n")
        
        ratings = div.find('div', attrs={'class':'inline-block ratings-imdb-rating'})
        print("The rating for this film is a: " + ratings.getText())
        
        description = div.find('p', attrs={'class':'text-muted'})
        print("The description: " + "\n" + description.find_next_siblings('p')[0].getText())
        
        
        bodyText = div.find('p', attrs={'class':'text-muted'})
        
        
        
        

        
        
        #print('the description of the movie is: ' + str(description2))
        #div = randMovie.find('div', attrs={'class':'lister-item-content'})
        #print(div)
        #header = randomDiv.findChildren('h3', attrs={'class':'lister-item-header'})
        
      
"""
        
        
        print('Your random movie is: ' + str((headers[0].findChildren('a'))[0].contents[0].encode('utf-8').decode('ascii', 'ignore')))
"""

                















