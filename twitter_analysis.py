import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("./tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!

for tweet in tweetData:
    #print (tweet ["text"])

    tb = TextBlob(tweet["text"])
    print(tb.polarity)


# Textblob sample:
#tb = TextBlob("tweets.json")
#print(tb.polarity)
