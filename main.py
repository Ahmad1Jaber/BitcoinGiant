import tweepy
import keys
import newsRequest
import status
from datetime import datetime
import json 

jsonFragmentation = 0
# Authenticate to Twitter
auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET_KEY)
auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_SECRET_TOKEN)
# Create API object
api = tweepy.API(auth)

# test authentication
try:
    api.verify_credentials()
    print(f"{status.bcolors.OK}(+) Authentication Successfull{status.bcolors.RESET}")
except:
    print(f"{status.bcolors.FAIL}(-) Authentication Failed{status.bcolors.RESET}")


JSONCallNews = newsRequest.callAPI()
JSONDataNews=JSONCallNews.get_JSON_News()
JSONCallPrice = newsRequest.callAPI()
JSONDataPrice=JSONCallPrice.get_JSON_Price()
today = datetime.today()
dtString = today.strftime("%d/%m/%Y %H:%M:%S")

for segment in range(19):
    counter=0
    fragmentedNews = JSONDataNews[segment]
    with open("twitter_record.json","r") as f:
        temp = json.load(f)
        for entry in temp:
            URL = entry["URL"]
            if URL==fragmentedNews['url']:
                counter+=1 
    if counter==0:
        item_data = {}
        with open("twitter_record.json","r") as f:
            temp = json.load(f)
        item_data["Title"] = fragmentedNews['title']
        item_data["URL"] = fragmentedNews['url']
        item_data["PublishedAt"] = fragmentedNews['publishedAt']
        item_data["Price"] = JSONDataPrice
        temp.append(item_data)
        with open("twitter_record.json","w") as f:
            tweet = fragmentedNews["title"] + " Price of Bitcoin on " + dtString + " " + fragmentedNews["url"] + " #bitcoin #bitcoinprice #bitcoinnews"   
            api.update_status(tweet)
            json.dump(temp,f,indent=5)
        break
# sql="INSERT INTO newsapi (Title,URL,ImageURL,PublishedAt,Price) VALUES (%s,%s,%s,%s,%s)"
# val = (fragmentedNews["title"],fragmentedNews["url"],fragmentedNews["urlToImage"], fragmentedNews["publishedAt"], JSONDataPrice)
# try:
#     connect = conn.connectAgent.connect()
#     mydb = connect.cursor()
#     mydb.execute(sql,val)
#     connect.commit()
#     print(f"{status.bcolors.OK}(+) ",mydb.rowcount,f"record inserted{status.bcolors.RESET}")
# except:
#     print(f"{status.bcolors.FAIL}(-) Inserted Failed{status.bcolors.RESET}")

#dbConnection.close()
#api.update_status("Testing Connection")



# sql="INSERT INTO newsapi (Title,URL,ImageURL,PublishedAt,Price) VALUES (%s,%s,%s,%s,%s)"
# val = (fragmentedNews["title"],fragmentedNews["url"],fragmentedNews["urlToImage"], fragmentedNews["publishedAt"], JSONDataPrice)
# try:
#     connect = conn.connectAgent.connect()
#     mydb = connect.cursor()
#     mydb.execute(sql,val)
#     connect.commit()
#     print(f"{status.bcolors.OK}(+) ",mydb.rowcount,f"record inserted{status.bcolors.RESET}")
# except:
#     print(f"{status.bcolors.FAIL}(-) Inserted Failed{status.bcolors.RESET}")

#dbConnection.close()
#api.update_status("Testing Connection")