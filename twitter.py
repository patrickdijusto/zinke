#import settings

import PyPDF2

##from folium 

#import folium
#import tweepy
#from textblob import TextBlob
import preprocessor as p
#from geopy.geocoders import Nominatim
#import random as rx

#print(folium.__version__)

# creating a pdf file object 
pdfFileObj = open('2018-10 Release Set 1 Doc 10.pdf', 'rb') 

# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

# printing number of pages in pdf file 
print(pdfReader.numPages) 

# creating a page object 
pageObj = pdfReader.getPage(0) 


text = pageObj.extractText().encode('utf-8')


print('DOI DAILY UPDATE' in text)
print("Home" in text)
print(True)
print(text.find('Home'))

# extracting text from page 
print(text) 

# closing the pdf file object 
pdfFileObj.close() 







def mx(a, b, c, d):
    '''Function to geocode the location data, perform sentiment analysis and plot on the map'''
    mapvar = folium.Map(location=[45.38, -121.67], zoom_start=3, width = 1200, height = 700)
    geolocator = Nominatim(user_agent = 'tweet_plot')
    # Row number
    i = 0
    try:
        for tweet in tweepy.Cursor(api.search, q=hashtag, lang="en", show_user=True).items():
            tweet_location = p.clean(tweet.user.location)
            print(tweet_location)
            try:
                location = geolocator.geocode(tweet_location)
            except:
                location = "NULL"
				
            if location == "None":
               location = "NULL"
			   
            # write in excel only if location is not null
            if location != "NULL" and tweet_location != '' and location is not None:
                # clean tweet
                type(tweet.text)
                lax = location.latitude +((rx.random()/100)-0.005)				
                lox = location.longitude +((rx.random()/100)-0.005)	
            
            
            tweet_text = p.tokenize(tweet.text.encode('UTF-8'))[2:]
            print(tweet_text)       
            print(location)
            print("\n")
            tip = folium.Tooltip(tweet.text, sticky=False)
            #print(".")
			
            # sentiment analysis
            feelings = TextBlob(tweet_text).sentiment.polarity
            icon = folium.Icon()
            if feelings >= 0:
                i = i + 1
                icon = folium.Icon(color='blue', icon = 'comment')
            elif feelings < 0:
                i = i + 1
                icon = folium.Icon(color='red')
				
            #lax = location.latitude +((rx.random()/100)-0.005)				
            #lox = location.longitude +((rx.random()/100)-0.005)				
				
            try:
                folium.Marker(location=[lax, lox], icon=icon, tooltip=tip).add_to(mapvar)
            except:
                pass
            if i == limiting_value:
                break
    except tweepy.error.TweepError:
        print("Check your credentials for correctness")
    mapvar.save('twittermap.html')
    
    
# if __name__ == '__main__':
    # '''INPUT YOUR CREDENTIALS HERE'''
    # # consumer_key = CONSUMER_KEY
    # # consumer_secret = CONSUMER_SECRET
    # # access_token = OAUTH_TOKEN
    # # access_secret = OAUTH_SECRET
OAUTH_TOKEN = "832776374603505664-0v91MI87pZKJrXBXditUsvnwfjr17MV"

OAUTH_SECRET = "qHYS33mXIABMC6jxkG7DdxS1ohM6VfTTZRmAyja0EK2qc"

CONSUMER_KEY = "kl4C3rLcKKPa1dlL1wlwPnxVh"

CONSUMER_SECRET = "CDdzJ3yVAKKSKLBN7If4Vxd9aAXGriVs7E5rdKjTNBtWrKmoMa"

	
##print(CONSUMER_KEY)
    
##mx(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_SECRET)
