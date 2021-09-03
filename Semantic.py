import json
import csv
import re
import string
import math

# Used Dicitionary to initialize word dictionary for snow, cold, flu with its entities.
searchingWordDict = {'snow': {
    "docsContainingPdf": 0,
    "docsPerAppeared": 0,
    "logDocsPerAppeared": 0,
    "metadata": {}
},
    'cold': {
    "docsContainingPdf": 0,
    "docsPerAppeared": 0,
    "logDocsPerAppeared": 0,
    "metadata": {}
},
    'flu': {
    "docsContainingPdf": 0,
    "docsPerAppeared": 0,
    "logDocsPerAppeared": 0,
    "metadata": {}
}
}

#filter.json file contains more than 3000 filtered Tweets
jsonfile = open('filter.json')

jsondata = json.load(jsonfile)
index = 0


highestFPerM = 0
highArc = ""
for tweet in jsondata:

    index = index + 1
    bag = re.split(" ", tweet['text'])
    # Used for task 3 to calculate f/m.
    temp = {
        "No of Article": index,
        "Article": tweet['text'],
        "wordCount": len(bag),
        "occurence": 0,
        "freqByWords": 0
    }

    for selectedWord in searchingWordDict:
        if selectedWord in bag:
            for word in bag:
                if word == selectedWord:
                    temp["occurence"] = temp["occurence"] + 1

            temp["freqByWords"] = temp["wordCount"]/temp["occurence"]
            if temp["freqByWords"] > highestFPerM:
                highArc = tweet['text']
                highestFPerM = temp["freqByWords"]
            searchingWordDict[selectedWord]["metadata"] = temp
            searchingWordDict[selectedWord]["docsContainingPdf"] = searchingWordDict[selectedWord]["docsContainingPdf"]+1


for word in searchingWordDict:
    if searchingWordDict[word]["docsContainingPdf"] != 0:
        searchingWordDict[word]["docsPerAppeared"] = round(100 /
                                                           (searchingWordDict[word]["docsContainingPdf"]), 2)

    if searchingWordDict[word]["docsPerAppeared"] != 0:
        searchingWordDict[word]["logDocsPerAppeared"] = round(math.log10(
            searchingWordDict[word]["docsPerAppeared"]), 2)

print("")
# Help for creating Table: https://www.delftstack.com/howto/python/data-in-table-format-python/

print("{:<13} |  {:<8} |  {:<8} |  {:<13} | ".format(
    'Search-Query', 'df', 'NByDf', 'logNByDf'))
for key, value in searchingWordDict.items():
    searchQuery, df, NByDf, logNByDf = value
    print("{:<13} |  {:<8} |  {:<8} |  {:<13} | ".format(
        key, searchingWordDict[key]["docsContainingPdf"], searchingWordDict[key]["docsPerAppeared"], searchingWordDict[key]["logDocsPerAppeared"]))
print("")

# Printing highest frequency article.
print("Highest Frequency Article : " + highArc)
