# Task 0:

* There are two inputs = call.csv & text.csv --> 2n
* Both inputs are used 3 times -->
```yaml
    reader = csv.reader(f)
    calls = list(reader)
    i, j, k, l = calls[-1]
```

* Remaining line of code = 4

### Big O Final   
O(3 * 2n + 4)

O(6n +4)

# Task 1:

* There are two inputs = call.csv & text.csv (n + n)

#### NOTE: Here I am calculating Big O of two inputs separately:

#### A. Big O for text.csv
length of text = 9072

First `for loop` has 3 lines
```yaml
    for i, j, k in texts:
        records.append(i)
        records.append(j)
```

Big O for first loop : (3x 9072)n

#### B. Big O for call.csv
length of calls = 5213

Second loop has 5 lines
```yaml
    for i, j, k, l in calls:
        if i not in records:
            records.append(i)
        if j not in records:
            records.append(i)
```

Big O for second loop:  (5 x 5213)n

#### Extra number of lines = 10

### Final Big O:

Big O = ( (3 * 9072)n + (5 * 5213)n + 10 )

# Task 2:

* There is only 1 input  i.e. calls.csv

* `for loop` has 11 lines of code from which 9 lines of code will always run:
```yaml
    for i, j, k, l in calls:
        call_1 = i.replace(" ", "")
        call_2 = j.replace(" ", "")
        if call_1 not in duration:
            duration[call_1] = int(l)

        # I have assumed that this will always run 
        else:
            # this can be skipped 
            duration[call_1] += int(l) 
        if call_2 not in duration:
            duration[call_2] = int(l)

        # I have assumed that this will always run
        else:
            # this can be skipped  
            duration[call_2] += int(l) 

```
* length of calls = 5213. This will be multiplied with 9n of ``for loop``

* extra line of code = 7

### Final Big O:

Big O = ( (5213 * 9n) + 7)

# Task 3

* Only 1 input i.e. calls.csv


* One of the `if statement` in `for loop` calls for a function `extract_areacode()`. I am assuming this is always called.
```yaml
def extract_areacode(n):
    p = n.replace("(", "").replace(")", "")
    return p[0:3]
```
* 6 lines in `for loop` will always be executed. Including the `extract_areacode()` function total lines executed become 9. i.e `9n`
```yaml
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
            else:
                marketers.append(receiver[0:3])
```

* length of calls = 5213. This will be multiplied with 9n of ``for loop``

* Remaining number of lines 13

* sorted unique function is ran - 3 times --> 3n 

### Final Big O:

Big O = ( (9n * 5213) + 3n  + 13)

# Task 4

* Only 1 input i.e. calls.csv

*  3 line in `for loop` are always executed. For worst case scenario I am assuming all the lines are executed i.e. 5n
```yaml
    for items in calls:
        caller = items[0]
        if '140' in caller[0:3]:
            if caller not in telemarketer:
                telemarketer.append(caller)
```

* length of calls = 5213. This will be multiplied with 5n of ``for loop``

*  Remaining lines are 10

### Final Big O:

Big 0 = ( (5n * 5213)  + 10 )
