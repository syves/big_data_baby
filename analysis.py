'''
The primary quantitative analysis that we would like to see is a [confusion matrix]
(http://en.wikipedia.org/wiki/Confusion_matrix) for each source, including
TP, FP, FN, and TN, accuracy, and any other metrics you find appropriate.
You should consider the labels assigned by the researchers to be ground 
truth and the labels given by the sources to be predictions. 

You should also present some subjective analysis of the results. For example:

*  Is accuracy the best metric for assessing these sources?
*  If we were to choose one of these two sources based on the results of this 
experiment, which one would you recommend and why?
'''
#read in the researcher files transform in memory to array of arrays
import csv
import json

def read_csv(filepath):
    companies = []
    with open(filepath) as csvfile:
        readable = csv.reader(csvfile)
        for row in readable:
            companies.append(row)
        return companies

andres = read_csv('/Users/syves/Documents/analyst_takehome/is_closed_classification_Andres.csv')
betty = read_csv('/Users/syves/Documents/analyst_takehome/is_closed_classification_Betty.csv')
craig = read_csv('/Users/syves/Documents/analyst_takehome/is_closed_classification_Craig.csv')
dana = read_csv('/Users/syves/Documents/analyst_takehome/is_closed_classification_Dana.csv')
elena = read_csv('/Users/syves/Documents/analyst_takehome/is_closed_classification_Elena.csv')

researcher_truths = andres + betty + craig + dana + elena
#each researcher has 40 unique companies, 200 companies total
#first array is [id, name, address, city, state, is_closed

#create nicer structure, dictrionary with keys, and boolean for is_closed for easy querying
truths = {id:{"id": id, "name":name, "is_closed": is_closed == 'Y'}
        for id, name, address, city, state, is_closed in researcher_truths}

#load json for access
with open('/Users/syves/Documents/analyst_takehome/hidden_info.json') as jsonfile:
#transform json object into dictionary of dictionaries, with is_close as boolean, and id as key
    predictions = {key: {"id": key,
                         "source": value["source"],
                         "is_closed": value["source_label_is_closed"] == "Y"}
                   for key, value in json.load(jsonfile).items()}

confusion_matrix = {"TP": 0, "FP": 0, "FN": 0, "TN": 0}

#keys common to both dictionaries
common_keys = set(truths.keys()).intersection(set(predictions.keys()))

for company_id in common_keys:
    # TP
    if (truths[company_id]["is_closed"] == True and predictions[company_id]["is_closed"] == True):
       # if (int(company["is_closed"]) == int( co["is_closed"])):
        confusion_matrix["TP"] += 1
    #FP
    elif (truths[company_id]["is_closed"] == False and predictions[company_id]["is_closed"] == True):
        confusion_matrix["FP"] += 1
    #FN
    elif (truths[company_id]["is_closed"] == True and predictions[company_id]["is_closed"] == False):
    #TN
        confusion_matrix["FN"] += 1
    else: #=> (truths[company_id]["is_closed"] == False and predictions[company_id]["is_closed"] == False):
        confusion_matrix["TN"] += 1

print confusion_matrix #=> {'FP': 54, 'TN': 1448, 'FN': 61, 'TP': 437}
print 54 + 1448 + 61 + 437 #=> 2000
print len(researcher_truths) #=> 2005
print researcher_truths[0]
print researcher_truths[1]
#find intersection of both dict somehow use shared key for comparison

