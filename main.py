from bs4 import BeautifulSoup as bsf
import requests
import re

# this class is useful for finding the general values
class local_vals():
    def __init__(self):
        self.__result = requests.get("https://www.worldometers.info/coronavirus/")
        self.__src = self.__result.content 
        self.__soup = bsf(self.__src, "html.parser")
        self.__mydivs = self.__soup.findAll("div", {"class": "maincounter-number"})
        self.__mydivs2 = self.__soup.findAll("div", {"class": "panel_front"})
        self.__mydivs3 = self.__soup.findAll("div",{"class":"number-table-main"})
        self.__values = re.findall(r"(?<=<span)[^>]*>(.*)<\/span>",str(self.__mydivs))
        self.__values2 = re.findall(r"(?<=<span)[^>]*>\n?(.*)<\/span>",str(self.__mydivs2))
        self.__values3 = re.findall(r"(?<=div)[^>]*>(.*?)<\/div>",str(self.__mydivs3))
        
    def get_locals(self,name):
        if name == "totalcases":
            return self.__values[0]
        elif name == "deaths":
            return self.__values[1]
        elif name == "recovered":
            return self.__values[2]
        elif name == "active":
            return self.__values3[0]
        elif name == "closed":
            return self.__values3[1]
        elif name == "mildcon":
            return self.__values2[0]
        elif name == "seriouscon":
            return self.__values2[1]
        else:
            raise ValueError("name is incorrect must be in parameters") 


