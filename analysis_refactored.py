import csv
import json
import os

#1.read in all the researcher files from directory
#2. and outputs combined to a researcher_data.csv?

#transform all researcher data into a iterable collection

def transform_researcher_data(filename):
    with open(filename) as csvfile:
        return {id: {"id": id, "name":name, "is_closed": is_closed == 'Y'}
                for id, name, address, city, state, is_closed in csv.reader(csvfile)}

def transform_source(filename):
    with open(filename) as jsonfile:
        return {id: {'id': id,
                     'source': value['source'],
                     'is_closed': value['source_label_is_closed'] == 'Y'}
                for id, value in json.load(jsonfile).items()}

def get_metrics(researcher_data, source_predictions):
    metrics = {}
    for company_id, prediction in source_predictions.items():
        source = prediction['source']
        is_closed = prediction['is_closed']

        if source not in metrics:
            metrics[source] = {'TP': 0, 'FP': 0, 'TN': 0, 'FN': 0}

        if (researcher_data[company_id]["is_closed"] and is_closed):
            # i want hash to have the name of company_id =>'RHSJEAKEF'
            metrics[source]["TP"] += 1
        elif (not researcher_data[company_id]["is_closed"] and is_closed):
            metrics[source]["FP"] += 1
        elif (researcher_data[company_id]["is_closed"] and not is_closed):
            metrics[source]["FN"] += 1
        else:
            metrics[source]["TN"] += 1
    return metrics

#how do I get these working now?
#get the right matrix
def accuracy(matrix):
    return float(matrix["TP"] + matrix["TN"]) / sum(matrix.values())

def true_positive_rate(matrix):
    return float(matrix["TP"]) / (matrix["TP"] + matrix["FN"])

def true_negative_rate(matrix):
    return float(matrix["TN"]) / (matrix["FP"] + matrix["TN"])

def positive_predictive_value(matrix):
    return float(matrix["TP"]) / (matrix["TP"] + matrix["FP"])

def negative_predictive_value(matrix):
    return float(matrix["TN"]) / (matrix["TN"] + matrix["FN"])

def false_positive_rate(matrix):
    return float(matrix["FP"]) / (matrix["FP"] + matrix["TN"])

def main():
    researcher_data = {}
    for f in os.listdir(os.path.join('data')):
        researcher_data.update(transform_researcher_data(os.path.join('data', f)))

    source_predictions = {}
    for f in os.listdir(os.path.join('sources')):
        source_predictions.update(transform_source(os.path.join('sources', f)))
    
        matrix = get_metrics(researcher_data, source_predictions)#=> {{}, {}}

    with open('analysis.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', quotechar=' ', escapechar=' ' ,quoting=csv.QUOTE_MINIMAL)
        for source in matrix:
        # out put source, matrix of source and other metrics to csv
            writer.writerows(
                    ['Source' + ':' + source + ','+
                         str(matrix[source])])
            for key, value in matrix.items():
                if key == source:
                #the other metrics
                    writer.writerows(
                   ['Accuracy'+ ':'  + str(accuracy(value)) + ', ' +
                    'TPR' + ':'  + str(true_positive_rate(value)) + ', ' +
                    'TRR' + ':'  + str(true_negative_rate(value)) + ', ' +
                    'PPV' + ':'  + str(positive_predictive_value(value)) + ', ' +
                    'NPV' + ':' + str(negative_predictive_value(value)) + ', ' +
                    'FPR' + ':'  + str(false_positive_rate(value))])

        return

if __name__ == '__main__':
    main()
