polarity = []
subjectivity = []


import json
from textblob import TextBlob
import numpy as np
import matplotlib.mlab as mlab
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

    polarity.append(tb.polarity)
    subjectivity.append(tb.subjectivity)

    
    bin_edges = [-1, -0.5, 0, 0.5, 1]
    plt.hist(polarity, bins=bin_edges)
    plt.xlabel ("polarity")
    plt.ylabel ("tweets")
    plt.show()





# Textblob sample:
#tb = TextBlob("tweets.json")
#print(tb.polarity)
