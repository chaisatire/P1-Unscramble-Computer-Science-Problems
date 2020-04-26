"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""

# with open('texts.csv', 'r') as f:
#     reader = csv.reader(f)
#     texts = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    duration = {}
    for i, j, k, l in calls:
        call_1 = i.replace(" ", "")
        call_2 = j.replace(" ", "")
        if call_1 not in duration:
            duration[call_1] = int(l)
        else:
            duration[call_1] += int(l)
        if call_2 not in duration:
            duration[call_2] = int(l)
        else:
            duration[call_2] += int(l)

number = max(duration, key=duration.get)

print('{} spent the longest time, {} seconds, on the phone during september 2016'.format(number, duration.get(number)))
