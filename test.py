import tweepy
import keys
import newsRequest
import status
from datetime import datetime
import json 

def writeData():
    item_data = {}
    with open("twitter_record.json","r") as f:
        temp = json.load(f)
    item_data["Title"] = "Hello World"
    item_data["URL"] = "https://www.ahmadjaber.com"
    item_data["PublishedAt"] = "22-07-2021"
    item_data["Price"] = "37,585.3256"
    temp.append(item_data)
    with open("twitter_record.json","w") as f:
        json.dump(temp,f,indent=5)
def findData(URL):
    with open("twitter_record.json","r") as f:
        temp = json.load(f)
        for entry in temp:
            URL = entry["URL"]
            if URL==URL:
                return -1
JSONCallNews = newsRequest.callAPI()
JSONDataNews=JSONCallNews.get_JSON_News()
JSONCallPrice = newsRequest.callAPI()
JSONDataPrice=JSONCallPrice.get_JSON_Price()
today = datetime.today()
dtString = today.strftime("%d/%m/%Y %H:%M:%S")

print(JSONDataNews)
counter=0
counter+=1
print(counter)