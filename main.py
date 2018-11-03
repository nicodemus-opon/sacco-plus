import tweepy
from textblob import TextBlob
import numpy as np
import pandas as pd
from datetime import *

consumer_key = "w1OfpL5GIeSEzQWAQbVRIrFvU"
consumer_secret = "iVrMsBaaIlCudtKiIhPBVu3onllfPuleGNoRxwJGHCj0agjtbT"
access_token = "1004781338841493505-vxy3uLUWSO3sL3Up4HllTg9djN4NdM"
access_token_secret = "SFaW44avqYqcZRGnIStuQmS8m4QL0F9wXrNmstytpBrDO"

## set up an instance of Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)



def main(queryx):
    global array_of_ids
    global array_of_comments
    global array_of_time
    global array_of_date
    global array_of_polarity
    global array_of_colors
    global mentions
    global average_sentiment

    array_of_stuff = []
    array_of_subs = []
    array_of_avgs = []
    array_of_dates = []

    array_of_ids = []
    array_of_comments = []
    array_of_time = []
    array_of_date = []
    array_of_polarity = []
    array_of_colors=[]

    ## Twitter credentials

    query = queryx
    max_tweets = 50
    searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
    try:
        for z in searched_tweets:
            try:
                time_created = z.created_at
                time_created_2 = str(time_created.date().strftime("%a-%d-%m-%y"))
                print(time_created_2)
                print(z.text)
                wiki = TextBlob(z.text)
                print(wiki.sentiment.polarity)
                if wiki.sentiment.polarity != 0.0:
                    array_of_stuff.append(wiki.sentiment.polarity)
                    tr_day = '"' + str(time_created_2) + '"'
                    array_of_dates.append(time_created_2)
                    array_of_comments.append(z.text)
                    array_of_time.append(str(time_created.time()))
                    array_of_date.append(str(time_created.date()))
                    pp = ""
                    if wiki.sentiment.polarity > 0:
                        array_of_polarity.append(str(float("{0:.2f}".format((1 + wiki.sentiment.polarity) * 50))) + " % positive")
                        array_of_colors.append("table-success")
                    else:
                        array_of_polarity.append(str(float("{0:.2f}".format((1 + wiki.sentiment.polarity) * 50))) + " % negative")
                        array_of_colors.append("table-danger")
                        # array_of_subs.append(wiki.sentiment.subjectivity)
                        # avgs=float((wiki.sentiment.polarity + wiki.sentiment.subjectivity)/2)
                        # array_of_avgs.append(avgs)
            except Exception as g:
                print(g)
                continue
    except Exception as e:
        print(e)

    x = 0.0
    try:
        for zy in array_of_stuff:
            zy += x
            x = zy
        zy = zy / len(array_of_stuff)
        # print("average=",str(zy),"%")
        perc = zy + 1
        cvf = perc / 2
        cvf = cvf * 100
        average_sentiment = (str(cvf), "%")
        mentions = int(len(array_of_stuff))
        ##
        y_plot = list(reversed(array_of_dates))
        x_plot = str(list(reversed(array_of_stuff)))
        array_of_ids = [de for de in range(len(x_plot))]
        return (y_plot, x_plot)
    except Exception as d:
        print(d)
    ##plt.plot([list(reversed(array_of_dates))[0],list(reversed(array_of_dates))[-1]],[list(reversed(array_of_stuff))[0],list(reversed(array_of_stuff))[-1]],color="green")
    ##plt.plot(range(len(array_of_subs)),array_of_subs,color="red")
    ##plt.plot(range(len(array_of_avgs)),array_of_avgs,color="green")
    ##plt.show()



def f_mentions():
    return mentions


def f_polarity():
    return array_of_polarity


def f_time():
    return array_of_time


def f_date():
    return array_of_date


def f_id():
    return array_of_ids


def f_comments():
    return array_of_comments


def f_colors():
    return array_of_colors


def f_average():
    return average_sentiment

#print(main("trump"))
#print(f_mentions())
