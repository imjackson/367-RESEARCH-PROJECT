### CISC367-010
### Group Members: Brianna Hunt, Debra Lymon, Jackson Pack
## concat_group_messages.py
#### This program (provided by Dr.Pollock and modified by us) allows users to input a disentangled xml chat file and create a csv (which groups conversations by conversation ids and concatenates consecutive utterances from same speaker in a conversation (adds semicolon between concatenated utterances). 
#### The output csv files of this program are in the 'original_xml_to_csv' folder.
## nltkanalysis.py
#### This program allows users to input a csv file of Slack chat data to perform sentiment analysis on each thread using NLTK Vader.
##### Users can input their chosen csv file name (we used the csv files from the 'original_xml_to_csv' folder).
##### For each thread, NLTK Vader Sentiment Analyzer is executed to determine the positivity scores of each thread.  
##### These results are output into a csv file pairing each thread number to its positivity scores.
##### The output csv files of this program are in the 'nltk_output_csv' folder.
