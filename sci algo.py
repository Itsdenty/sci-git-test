import time

def firstAlgo():
    my_string = "I am developing something much awaited, something the whole world will enjoy so we can all have a wonderful good time"
    new_string = my_string.split(" ")
    previous_length = 0
    highest = ""
    for current_string in new_string:
        current_length = len(current_string)
        if current_length > previous_length:
            highest = current_string
            previous_length = current_length
    print highest


def secondAlgo():
    my_string = "I am developing something much awaited, something the whole world will enjoy so we can all have a wonderful good time"
    new_string = my_string.split(" ")
    sort_string = lambda a, b: a if (len(a) > len(b)) else b
    highest = reduce(sort_string, new_string)
    print highest

# t0 = time.clock()
# firstAlgo()
# t1 = time.clock()
# print t1 - t0
# print t1, t0

t3 = time.clock()
secondAlgo()
t4 = time.clock()
print t4-t3


