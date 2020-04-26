"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def extract_areacode(n):
    p = n.replace("(", "").replace(")", "")
    return p[0:3]


def sorted_unique(n):
    numbers = list(dict.fromkeys(n))
    sorted_list = sorted(numbers)
    return sorted_list


def create_number_list(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)
    landline = []
    mobile = []
    bangalore = []
    for items in calls:
        caller = items[0]
        receiver = items[1]
        if '(080)' in caller:
            if '(080)' in receiver:
                bangalore.append(receiver)
            elif '(' in receiver:
                landline.append(extract_areacode(receiver))
            elif '140' not in receiver[0:3]:
                mobile.append(receiver[0:4])

    return sorted_unique(landline), sorted_unique(mobile), sorted_unique(bangalore)


landline, mobile, bangalore = create_number_list('calls.csv')

percentage = 100 * (len(bangalore) / (len(bangalore) + len(landline) + len(mobile)))

print("The numbers called by people in Bangalore have codes:\n{}".format("\n".join(landline + mobile)))

print("\n{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
    percentage))

