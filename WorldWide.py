import requests
from bs4 import BeautifulSoup as bsf
import re
# worldwide class results the output of the worldwide data
class WorldWide():


    def __init__(self):
        # local variables do not edit
        self.__result = requests.get("https://www.worldometers.info/coronavirus/")
        self.__src = self.__result.content 
        self.__soup = bsf(self.__src, "html.parser")
        self.__mydivs = self.__soup.findAll("tr", {"style": ""})
        self.__li=list() # list to append all the dictionaries

        # for every element in result set formed by findAll method check for the matches
        for tr in range(202,len(self.__mydivs)):
            self.__values = re.findall(r"(.*?><a.*?>(.*?)<|(?<=<td).*>(.*)<\/td>)",str(self.__mydivs[tr])) #regex statement
            
            # check if the result set found no values matched 
            if len(self.__values) != 0:
                dictr={} #empty dictionary after every loop
                dictr["number"] = (self.__values[0][1].strip()+" "+self.__values[0][2].strip())
                dictr["country"] = (self.__values[1][1].strip()+" "+self.__values[1][2].strip())
                dictr["total cases"]= (self.__values[2][1].strip()+" "+self.__values[2][2].strip())
                dictr["new cases"] = (self.__values[3][1].strip()+" "+self.__values[3][2].strip())
                dictr["total deaths"] = (self.__values[4][1].strip()+" "+self.__values[4][2].strip())
                dictr["total recovered"] = (self.__values[5][1].strip()+" "+self.__values[5][2].strip())
                dictr["active cases"] = (self.__values[6][1].strip()+" "+self.__values[6][2].strip())
                dictr["serious cases"] = (self.__values[7][1].strip()+" "+self.__values[7][2].strip())
                dictr["totalcases/m"] = (self.__values[8][1].strip()+" "+self.__values[8][2].strip())
                dictr["deaths/m"] = (self.__values[9][1].strip()+" "+self.__values[9][2].strip())
                dictr["total tests"] = (self.__values[10][1].strip()+" "+self.__values[10][2].strip())
                dictr["tests/m"] = (self.__values[11][1].strip()+" "+self.__values[11][2].strip())
                dictr["population"] = (self.__values[12][1].strip()+" "+self.__values[12][2].strip())
                dictr["continent"] = (self.__values[13][1].strip()+" "+self.__values[13][2].strip())
                self.__li.append(dictr) # append the matched dictionary
    

    # this function returns dictionary with all the fields
    def get_data(self, country):
        for i in self.__li:
            if i['country'].strip() == country:
                return i
        else:
            raise ValueError("The coutry name does not exist")