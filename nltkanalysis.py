# CISC367-010
# Group Members: Brianna Hunt, Debra Lymon, Jackson Pack
# Programmed by Debra Lymon
# This program takes in a csv file containing threads from Slack communities
# The data is placed in a DataFrame using pandas for easier access/organization
# The data is re-grouped by thread number in the DataFrame
# Then, for each thread, NLTK Vader Sentiment Analyzer is executed to determine the positivity scores of each thread
# These results are output into a csv file pairing each thread number to its positivity scores


import nltk
import pandas as pd
import csv
from itertools import zip_longest
import numpy as np
from nltk.sentiment import SentimentIntensityAnalyzer
#nltk.download()

filepath = input("Enter csv filename: ") #make sure to include .csv extension
og_data = pd.read_csv(filepath) #reading original csv data into a DataFrame
data = (og_data.groupby('thread')).first() #indexed by thread number
scores=[]
thread_index = []
labels=[]
pos_scores=[]

# Running NLTK Vader Sentiment Analyzer on each thread
# returns
def nltk_thread(data):
    for ind in data.index: #data is indexed (grouped) by thread
        sia = SentimentIntensityAnalyzer()
        output = sia.polarity_scores(data.message[ind])
        num1 = output.get('compound')
        if num1 > 0: #if compound > 0, it is positive
            largest = 'pos'
        elif num1 < 0: #if compound < 0, it is negative
            largest = 'neg'
        else:
            largest = 'neu' #if compound = 0, it is neutral

        pos_scores.append(output.get('pos')) #store pos scores
        labels.append(largest) #store thread label
        scores.append(output) #store score dictionaries in list
        thread_index.append(ind) #store thread num in list


def main():
    nltk_thread(data)

    #write to csv file
    thread = thread_index
    positivity_score = scores
    csv_data = [thread, positivity_score, labels, pos_scores]
    export_data=zip_longest(*csv_data, fillvalue = '')
    write_filepath = input("Enter file name you would like to save as: ") #Enter with .csv extension included
    with open(write_filepath, 'w', encoding="ISO-8859-1", newline='') as file:
        write = csv.writer(file)
        write.writerow(("Thread", "Sentiment Scores", "Label", "Positive Score"))
        write.writerows(export_data)


if __name__ == "__main__":
    main()