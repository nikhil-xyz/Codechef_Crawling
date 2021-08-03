from bs4 import BeautifulSoup
import requests

class Manager:
    soup = ""
    def setUserId(user_id):
        page = requests.get("https://www.codechef.com/users/"+user_id)
        global soup
        soup = BeautifulSoup(page.content, 'html.parser')
        # print(soup)

    def getUserName(self):
        name = soup.find(class_='h2-style')
        return str(name.text)

    def getUserRating(self):
        rating = soup.find(class_="rating-number")
        return str(rating.text)

    def getCountry(self):
        country = soup.find("span", class_="user-country-name")
        return str(country.text)

    def fullySolvedProblems(self):
        title = soup.select("h5", class_="rating-data-section problems-solved")[0]
        print(title.text)
        temp = soup.select("article", class_="rating-data-section problems-solved")[0]
        for i in range(len(temp)):
            data = temp.select("p")[i].select("span a")
            for x in data:
                print(x.text)
            print("")
        print("________________________")

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
