import keys
import requests
from datetime import date
import os
import status
from abc import ABCMeta,abstractstaticmethod

class newRequest(metaclass=ABCMeta):

    @abstractstaticmethod
    def request():
        """API Request Interface"""


class day_Request(newRequest):
    def __init__(self):
        self.today = date.today()
        self.dayFormat = self.today.strftime("%Y-%m-%d")
    def request(self):
        return self.dayFormat


class callNews(newRequest):
    def __init__(self):
        day = callAPI()
        currentDate=day.get_Day()
        try:
            self.response = requests.get("https://newsapi.org/v2/everything?q=Cryptocurrency&from="+currentDate+"&sortBy=&apiKey="+keys.api_key_news)
            self.segementJson = self.response.json()["articles"]
            print(f"{status.bcolors.OK}(+) Get NewsAPI Succefull{status.bcolors.RESET}")

        except:
            print(f"{status.bcolors.FAIL}(-) Get NewsAPI Failed{status.bcolors.RESET}")

    def request(self):
        return self.segementJson

class callPrice(newRequest):
    def __init__(self):
        try:
            self.response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            self.segementJson = self.response.json()["bpi"]["USD"]["rate"]
            print(f"{status.bcolors.OK}(+) Get Price Succefull{status.bcolors.RESET}")

        except:
            print(f"{status.bcolors.FAIL}(-) Get Price Failed{status.bcolors.RESET}")

    def request(self):
        return self.segementJson

class callAPI():
    #Get Day
    @staticmethod
    def get_Day():
        try:
            day = day_Request()
            currentDay= day.request()
            return currentDay
            raise AssertionError("Failed to get request")
        except AssertionError as _e:
            print(_e) 
    #Get JSON Data
    @staticmethod
    def get_JSON_News():
        try:
            JSON = callNews()
            JSONGetData= JSON.request()
            return JSONGetData
            raise AssertionError("Failed to get request")
        except AssertionError as _e:
            print(_e) 
    @staticmethod
    def get_JSON_Price():
        try:
            JSON = callPrice()
            JSONGetData= JSON.request()
            return JSONGetData
            raise AssertionError("Failed to get request")
        except AssertionError as _e:
            print(_e) 

if __name__ == "__main__":
    """Main Section"""
    # JSONCallNews = callAPI()
    # JSONDataNews=JSONCallNews.get_JSON_News()
    # print(JSONDataNews)
    # JSONCallPrice = callAPI()
    # JSONDataPrice=JSONCallPrice.get_JSON_Price()
    # #print(JSONDataPrice)