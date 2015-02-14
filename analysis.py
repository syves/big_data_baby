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
#each researcher has 401 unique companies, 2005 companies total

#create nicer structure, dictrionary with keys, and boolean for is_closed for easy querying
truth = {id:{"id": id, "name":name, "is_closed": is_closed == 'Y'}
        for id, name, address, city, state, is_closed in researcher_truths}

print truth

with open('/Users/syves/Documents/analyst_takehome/hidden_info.json') as jsonfile:
    print json.load(jsonfile)

#for each company in truths: 
    #get each source prediction


