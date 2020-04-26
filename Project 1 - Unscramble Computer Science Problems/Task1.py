"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

import csv

records = []

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for i, j, k in texts:
        records.append(i)
        records.append(j)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for i, j, k, l in calls:
        if i not in records:
            records.append(i)
        if j not in records:
            records.append(i)
    uniq_records = set(records)

print('There are {} different telephone numbers in the records'.format(len(uniq_records)))
