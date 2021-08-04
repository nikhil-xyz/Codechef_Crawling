#This file will retrieve the information from the source code of the webpage
from bs4 import BeautifulSoup
import requests

class Manager:
    soup = ""   #this variable will store the sourcecode 
    def setUserId(user_id):
        page = requests.get("https://www.codechef.com/users/"+user_id)  #user_id is being received
        global soup #making variable global to access source code from other available functions
        soup = BeautifulSoup(page.content, 'html.parser')   #"html-parser" will format raw code to HTML
        # print(soup)

    # find() method of BeautifulSoup will be used to extract attribute value using name given in HTML sourcecode file  
    def getUserName(self):
        name = soup.find(class_='h2-style') 
        return str(name.text)

    def getUserRating(self):
        rating = soup.find(class_="rating-number")
        return str(rating.text)

    def getCountry(self):
        country = soup.find("span", class_="user-country-name")
        return str(country.text)

    # this function will print all the fully solved problem-codes.
    def fullySolvedProblems(self):
        title = soup.select("h5", class_="rating-data-section problems-solved")[0]
        print(title.text)
        
        # loop will be used to traverse all the child elements
        temp = soup.select("article", class_="rating-data-section problems-solved")[0]
        for i in range(len(temp)):
            data = temp.select("p")[i].select("span a")
            for x in data:
                print(x.text)
            print("")
        print("________________________")

    # this function will print all the partially solved problem-codes.
    def partiallySolvedProblems(self):
        title = soup.select("h5", class_="rating-data-section problems-solved")[1]
        print(title.text)
        temp = soup.select("article", class_="rating-data-section problems-solved")[1]
        try:
            for i in range(len(temp)):
                data = temp.select("p")[i].select("span a")
                for x in data:
                    print(x.text)
                print("")
        except:
            pass
        print("________________________")
