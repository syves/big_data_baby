import csv
import json
import os

#1.read in all the researcher files from directory
#2. and outputs combined to a researcher_data.csv?

#transform all researcher data into a iterable collection
#now all researchers are in one file, each row is a company
'''
def helper_transform_researchers_data():
    files = os.listdir('data') #=> ['file.csv', 'file2.csv']
   # print files
    companies = []
    #or should I do all the files in analyst_takehome
#and for file in files.endswith('.csv')
    for file in files:
        #print file
        #print os.path.abspath(file)
        with open(os.path.abspath(file)) as csvfile:
            #=> '/Users/syves/Documents/analyst_takehome/is_closed_classification_Andres.csv'
    #should be '/Users/syves/Documents/analyst_takehome/data/is_closed_classification_Andres.csv'
            readable = csv.reader(csvfile)
            for row in readable:
                companies.append(row)
        #transform array into dictionary
        return {id:{"id": id, "name":name, "is_closed": is_closed == 'Y'}
                        for id, name, address, city, state, is_closed in companies}
print helper_transform_researchers_data()
'''

def helper_transform_sources():
    files = os.listdir('analyst_takehome')
    print files #=> ['hidden_info.json']
    print os.path.isdir('sources')#=> TRUE

    for file in files:
        if file.endswith('.json'):
            with open(os.path.abspath(file)) as jsonfile:
            #transform json object into dictionary of dictionaries, with is_close as boolean, and id as key
                return {key: {"id": key,
                              "source": value["source"],
                              "is_closed": value["source_label_is_closed"] == "Y"}
                            for key, value in json.load(jsonfile).items()}
    #returns predictions which is an ungrouped collection of source data. Maybe its not necesary to sort them?
    #simple increment count of confusion matrix metric as it occurs?
print helper_transform_sources()

'''
def helper_metrics()
    metrics = []
    #metric {"TP": 0, "FP": 0, "FN": 0, "TN": 0, "accuracy": , ...}

    #keys common to both dictionaries
    common_keys = set(helper_transform_sources.keys()).intersection(set(helper_combine_researchers.keys()))

    for company_id in common_keys:
        #create a matrix dict for company if one does not exist 
        # ...
        #else increment value or key
        metric["Accuracy"] = float(metric["TP"] + metric["TN"]) / metric["TP"] + metric["FN"] + metric["FP"] + metric["TN"] )
        metric["True_positive_rate"] = float(metric["TP"]) / (metric["TP"] + metric["FN"])
        metric["True_negative_rate"] = float(metric["TN"]) / (metric["FP"] + metric["TN"])
        metric["Positive_predictive_value"] = float(metric["TP"]) / (metric["TP"] + metric["FP"])
        metric["Negative_predictive_value"] = float(metric["TN"]) / (metric["TN"] + metric["FN"])
        metric["False_positive_rate"] = float(metric["FP"]) / (metric["FP"] + metric["TN"])
        # TP
        if (helper_combine_researchers()[company_id]["is_closed"] == True and helper_transform_sources()[company_id]["is_closed"] == True):
            metric["TP"] += 1
        #FP
        elif (helper_combine_researchers()[company_id]["is_closed"] == False and helper_transform_sources()[company_id]["is_closed"] == True):
            metric["FP"] += 1
        #FN
        elif (helper_combine_researchers()[company_id]["is_closed"] == True and helper_transform_sources()[company_id]["is_closed"] == False):
        #TN
            metric["FN"] += 1
        else:
            metric["TN"] += 1
    return metrics


def main('path to parent?')
    #helper_transform_researchers_data('everything in data') 
    #helper_transform_sources('everything in sources') 
       
       #=>>> outputs metrics to Analysis.csv

pass

#main('some path')
'''
