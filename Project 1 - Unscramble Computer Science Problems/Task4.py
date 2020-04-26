"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

# with open('texts.csv', 'r') as f:
#     reader = csv.reader(f)
#     texts = list(reader)
#
# with open('calls.csv', 'r') as f:
#     reader = csv.reader(f)
#     calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def telemarketers_list(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)
    telemarketer = []
    for items in calls:
        caller = items[0]
        if '140' in caller[0:3]:
            if caller not in telemarketer:
                telemarketer.append(caller)
    telemarketer = sorted(telemarketer)
    return telemarketer

telemarketers_list('calls.csv')

print('This numbers could be telemarketers: \n{}'.format("\n".join(telemarketers_list('calls.csv'))))
