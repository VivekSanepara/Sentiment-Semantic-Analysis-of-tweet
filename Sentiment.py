import re
import string
import json
import csv

# filter.json contains more than 3000 filtered tweets
jsonfile = open('filter.json')


jsondata = json.load(jsonfile)
index = 0
# print ("{:<10} {:<10} {:<10} {:<10}".format('TWEET', 'MESSAGE', 'MATCH','POLARITY'))
for tweet in jsondata:

    index = index + 1
    # Initialize dictionary with all the entities required 
    temp = {
        "tweet": index,
        "message": tweet['text'],
        "bag": {},
        "match": [],
        "polarity": "",
        "positive": 0,
        "negative": 0
    }
    bag = re.split(" ", tweet['text'])

    for word in bag:
        if word not in temp["bag"]:
            temp["bag"][word] = 0
        temp["bag"][word] += 1

    # Compare with positive and negative words and add it to the Compare list
    # https://positivewordsresearch.com/list-of-positive-words/
    with open('positive.txt', 'r') as f:
        for line in f:
            for word in line.split():
                if word in bag:
                    temp["match"].append(word)
                    temp['positive'] = temp['positive']+1

    # https://positivewordsresearch.com/list-of-negative-words/
    with open('negative.txt', 'r') as f:
        for line in f:
            for word in line.split():
                if word in bag:
                    temp["match"].append(word)
                    temp['negative'] = temp['negative']+1

    #defining Polarity
    if temp["positive"] > temp['negative']:
        temp["polarity"] = "positive"
    elif temp["positive"] < temp['negative']:
        temp["polarity"] = "negative"
    else:
        temp["polarity"] = "neutral"

    print(temp["tweet"],'| Message: ',temp["message"],'| Match words: ', temp["match"],'| Polarity:',temp["polarity"])

    if index == 100:
        break
