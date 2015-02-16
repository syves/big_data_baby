'''
The primary quantitative analysis that we would like to see is a [confusion matrix]
(http://en.wikipedia.org/wiki/Confusion_matrix) for each source, including
TP, FP, FN, and TN, accuracy, and any other metrics you find appropriate.
You should consider the labels assigned by the researchers to be ground
truth and the labels given by the sources to be predictions.
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
#each researcher has 400 unique companies, 2000 companies total
#first array is [id, name, address, city, state, is_closed]

#create nicer structure, dictionary with keys, and boolean for is_closed for easy querying
truths = {id:{"id": id, "name":name, "is_closed": is_closed == 'Y'}
        for id, name, address, city, state, is_closed in researcher_truths}

#load json for access
with open('/Users/syves/Documents/analyst_takehome/hidden_info.json') as jsonfile:
#transform json object into dictionary of dictionaries, with is_close as boolean, and id as key
    predictions = {key: {"id": key,
                         "source": value["source"],
                         "is_closed": value["source_label_is_closed"] == "Y"}
                   for key, value in json.load(jsonfile).items()}

#seperate sources
Verifidelity = dict([company for company in predictions.items() if company[1]["source"] == "Verifidelity"])
Accutronix = dict([company for company in predictions.items() if company[1]["source"] == "Accutronix"])


def confusion_matrix(source):
    confusion_matrix = {"TP": 0, "FP": 0, "FN": 0, "TN": 0}

    #keys common to both dictionaries
    common_keys = set(truths.keys()).intersection(set(source.keys()))

    for company_id in common_keys:
        # TP
        if (truths[company_id]["is_closed"] == True and source[company_id]["is_closed"] == True):
           # if (int(company["is_closed"]) == int( co["is_closed"])):
            confusion_matrix["TP"] += 1
        #FP
        elif (truths[company_id]["is_closed"] == False and source[company_id]["is_closed"] == True):
            confusion_matrix["FP"] += 1
        #FN
        elif (truths[company_id]["is_closed"] == True and source[company_id]["is_closed"] == False):
        #TN
            confusion_matrix["FN"] += 1
        else: #=> (truths[company_id]["is_closed"] == False and predictions[company_id]["is_closed"] == False):
            confusion_matrix["TN"] += 1
    return confusion_matrix

#This is not dry, with more time I would  might refactor this section
def accuracy(matrix, source):
    common_keys = set(truths.keys()).intersection(set(source.keys()))
    return "Accuracy: " + str(float(matrix["TP"] + matrix["TN"]) / sum(matrix.values()))

def true_positive_rate(matrix, source):
    common_keys = set(truths.keys()).intersection(set(source.keys()))
    return "true_positive_rate: " + str(float(matrix["TP"]) / (matrix["TP"] + matrix["FN"]))

def true_negative_rate(matrix, source):
    common_keys = set(truths.keys()).intersection(set(source.keys()))
    return "true_negative_rate: " + str(float(matrix["TN"]) / (matrix["FP"] + matrix["TN"]))

def positive_predictive_value(matrix, source):
    common_keys = set(truths.keys()).intersection(set(source.keys()))
    return "positive_predictive_value: " + str(float(matrix["TP"]) / (matrix["TP"] + matrix["FP"]))

def negative_predictive_value(matrix, source):
    common_keys = set(truths.keys()).intersection(set(source.keys()))
    return "negative_predictive_value: " + str(float(matrix["TN"]) / (matrix["TN"] + matrix["FN"]))

def false_positive_rate(matrix, source):
    common_keys = set(truths.keys()).intersection(set(source.keys()))
    return "false_positive_rate: " + str(float(matrix["FP"]) / (matrix["FP"] + matrix["TN"]))


#________________________________________________________________________________________________________
print "Verifidelity Confusion Matrix:"
print confusion_matrix(Verifidelity)
print accuracy(confusion_matrix(Verifidelity), Verifidelity)
print true_positive_rate(confusion_matrix(Verifidelity), Verifidelity)
print true_negative_rate(confusion_matrix(Verifidelity), Verifidelity)
print positive_predictive_value(confusion_matrix(Verifidelity), Verifidelity)
print negative_predictive_value(confusion_matrix(Verifidelity), Verifidelity)
print false_positive_rate(confusion_matrix(Verifidelity), Verifidelity)

print " "
print "Accutronix Confusion Matrix:"
print confusion_matrix(Accutronix)
print accuracy(confusion_matrix(Accutronix), Accutronix)
print true_positive_rate(confusion_matrix(Accutronix), Accutronix)
print true_negative_rate(confusion_matrix(Accutronix), Accutronix)
print positive_predictive_value(confusion_matrix(Accutronix), Accutronix)
print negative_predictive_value(confusion_matrix(Accutronix), Accutronix)
print false_positive_rate(confusion_matrix(Accutronix), Accutronix)


'''
Verifidelity Confusion Matrix:
{'FP': 13, 'TN': 693, 'FN': 52, 'TP': 242}
Accuracy: 0.935
true_positive_rate: 0.823129251701
true_negative_rate: 0.981586402266
positive_predictive_value: 0.949019607843
negative_predictive_value: 0.930201342282
false_positive_rate: 0.0184135977337
 
Accutronix Confusion Matrix:
{'FP': 41, 'TN': 755, 'FN': 9, 'TP': 195}
Accuracy: 0.95
true_positive_rate: 0.955882352941
true_negative_rate: 0.948492462312
positive_predictive_value: 0.826271186441
negative_predictive_value: 0.988219895288
false_positive_rate: 0.0515075376884'''


