import re
from bs4 import BeautifulSoup
import urllib3
from random import choice, randint
from theLinks import pageFinder

#random num generator in case user wants random genre
randNum1 = randint(1,24)
print(randNum1)


# getting genre preference from the user/option to choose random genre
genrePicker = input("What genre would you like? You can also type random for a random genre ")
if genrePicker == 'random':
        genrePicker = str(randNum1)
               
#some whitespace for cleanliness
print("\n")

#user selects whether they want a random movie in their chosen genre, or if they want the top 50 list.
userSelection = input("Would you like a random movie, or the top 50 from your selection? ")
                 

#if the user selects the top 50 list
if userSelection.lower() == "top 50" or userSelection == "top" or userSelection == "50":
        #whitespace
        print("\n")
        print("\n")
        
        
        #parsing through the HTML of the genre page the user selected/was given.
        i = 1
        
        #condensing all divs with the class lister-item mode-advanced into a movielist
        movieList = pageFinder(genrePicker.lower()).findAll('div', attrs={'class': 'lister-item mode-advanced'})
        
        #for loop to iterate through the movie list in order to print the top 50 titles in the genre.
        for div_item in movieList:
                div = div_item.find('div', attrs={'class':'lister-item-content'})
                print(str(i) + '.'),
                
                #selecting the actual title of the film via h3
                header = div.findChildren('h3', attrs={'class':'lister-item-header'})
                #using findChildren find and isolate the title link in a readable format.
                print('Movie: ' + str((header[0].findChildren('a'))[0].contents[0].encode('utf-8').decode('ascii', 'ignore')))
                
                i += 1
                                 

#if the user chose a random movie
elif userSelection.lower() == "random" or userSelection.lower() == "random movie":
        #whitespace
        print("\n")
        print("\n")
        
        #using the choice function in the random module to select a random film from the movie list
        movieList = pageFinder(genrePicker.lower()).findAll('div', attrs={'class': 'lister-item mode-advanced'})
        randMovie = choice(movieList)
        
        #condensing the random movie via finding divs with the class name lister-item-content
        div = randMovie.find('div', attrs={'class':'lister-item-content'})
        
        #getting and printing the title of the random movie as above
        header = div.findChildren('h3', attrs={'class':'lister-item-header'})
        print('Your random movie is called: '  + str((header[0].findChildren('a'))[0].contents[0].encode('utf-8').decode('ascii', 'ignore')))
        
        print("\n")
        
        #isolating the numerical rating provided by searching for the inline-block ratings-imdb-rating class
        ratings = div.find('div', attrs={'class':'inline-block ratings-imdb-rating'})
        
        #using the getText function to isolate the numbers from the tags
        print("The rating for this film is a: " + ratings.getText())
        
        #getting and printing the description of the film by using the find_next_siblings and getText functions
        description = div.find('p', attrs={'class':'text-muted'})
        print("The description: " + "\n" + description.find_next_siblings('p')[0].getText())
        

        
        
        
        

        
        









