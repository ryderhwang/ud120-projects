#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print len (enron_data)
print len (enron_data['METTS MARK'])
count = 0
for k in enron_data :
    if enron_data[k]['poi'] :
        count += 1
print count

count = 0
for k in enron_data :
    if enron_data[k]['salary'] != 'NaN' :
        count += 1
print count

count = 0
for k in enron_data :
    if enron_data[k]['email_address'] != 'NaN' :
        count += 1
print count

count  = 0
for k in enron_data :
    if enron_data[k]['total_payments'] == 'NaN' and enron_data[k]['poi'] :
        count += 1
print (float(count) / 21)

count  = 0
for k in enron_data :
    if enron_data[k]['total_payments'] == 'NaN' :
        count += 1
print (float(count) / 21)

poi_names = open("../final_project/poi_names.txt").read().split('\n')
poi_y = [name for name in poi_names if "(y)" in name or "(n)" in name]
print len (poi_y)

print (enron_data['PRENTICE JAMES'])
print (enron_data['COLWELL WESLEY'])
print (enron_data["SKILLING JEFFREY K"])
SKILLING = enron_data["SKILLING JEFFREY K"]["total_payments"]
LAY = enron_data["LAY KENNETH L"]["total_payments"]
FASTOW = enron_data["FASTOW ANDREW S"]["total_payments"]

print SKILLING
print LAY
print FASTOW
