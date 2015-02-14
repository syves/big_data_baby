# Radius Takehome - Analyst Role

We offer this takehome assignment for a few reasons: 

1.  We would like to get a sense of your coding ability and style as well as your approach to solving a problem.
2.  We would like you to get a sense for something that an analyst at Radius might be expected to do.
3.  It is an opportunity for you to sharpen your coding/analysis skills and perhaps learn something new!

You should be able to complete this takehome within a few hours. You should use Python to complete the task, but you are welcome to use any standard libraries or modules that you find helpful.

## The Assignment
The primary purpose of the assignment is to produce an analysis of the results of a fictional (but realistic) experiment. We conduct many of these experiments in an effort to validate the accuracy of our data sources as well as our own data product. 

### The Experiment
This experiment is designed to test the accuracy of two prospective (fictional) data sources, "Accutronix" and "Verifidelity". In particular, we are interested in one specific field: `is_closed`. This field tells us if a company has gone out of business, which is an essential piece of information!

To conduct the experiment we sampled 1000 records from each source, reduced each record to only the fields necessary for a person to assess if the business is still alive, and prepared spreadsheets containing that information. Because we want to minimize experimental bias, we hide the source labels and source names from the people who fill out these spreadsheets (but retain that information in a separate file for later analysis). 

### The Data

* The `hidden_info.json` file contains the source name and label for each example, keyed by a unique ID. 
* The 5 `is_closed_classification_{name}.csv` files contain rows of record information. The `is_closed` column contains that person's assessment of whether the business is open or closed. The `unique_id` column can be used to connect each example to the information about it contained in the hidden data file. The other columns are irrelevant to your analysis. 

### The Analysis
The primary quantitative analysis that we would like to see is a [confusion matrix](http://en.wikipedia.org/wiki/Confusion_matrix) for each source, including TP, FP, FN, and TN, accuracy, and any other metrics you find appropriate. You should consider the labels assigned by the researchers to be ground truth and the labels given by the sources to be predictions. 

You should also present some subjective analysis of the results. For example:

*  Is accuracy the best metric for assessing these sources?
*  If we were to choose one of these two sources based on the results of this experiment, which one would you recommend and why?

### Extra Credit
If you finish the assignment quickly, feel free to attempt some of these additional challenges to show off your skills!

1.  Visualizations
2.  Confidence intervals

## Submission of Work
Please submit at least these two files:

1.  analysis.py - A python file containing all code you wrote to compile the analysis.
2.  analysis.txt (or .md) - A text file describing your results and any extra analysis of the experiment. 

If you produce any additional work, please include that as well!