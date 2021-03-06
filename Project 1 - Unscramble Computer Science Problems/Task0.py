"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    i, j, k = texts[0]
    print('first record of texts, {} texts {} at time {}'.format(i, j, k.split()[1]))

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    i, j, k, l = calls[-1]

    print('last record of calls, {} calls {} at time {}, lasting {} seconds '.format(i, j, k.split()[1], l))
