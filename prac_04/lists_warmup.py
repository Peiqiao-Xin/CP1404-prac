"""

    SET numbers TO [3, 1, 4, 1, 5, 9, 2]

    GET numbers[0]              first element
    GET numbers[-1]             last element
    GET numbers[3]              element at index 3

    GET numbers[0 .. -2]        all elements except the last
    GET numbers[3 .. 3]         sub-list from index 3 up to (but not including) 4

    EVALUATE (5 IN numbers)     returns TRUE or FALSE
    EVALUATE (7 IN numbers)     returns TRUE or FALSE
    EVALUATE ("3" IN numbers)   returns TRUE or FALSE

    SET new_list TO numbers + [6, 5, 3]

    SET numbers[0] TO "ten"     replace first element
    SET numbers[-1] TO 1        replace last element

    GET numbers[2 .. END]       all elements except the first two
    EVALUATE (9 IN numbers)     returns TRUE or FALSE
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# What values do the following expressions have?
# (solutions not provided; figure it out, then run with print or in console to test)
numbers[0]
numbers[-1]
numbers[3]
numbers[:-1]
numbers[3:4]
5 in numbers
7 in numbers
"3" in numbers
numbers + [6, 5, 3]

# Write Python expressions (in your Python file) to achieve the following:

# Change the first element of numbers to "ten"
numbers[0] = "ten"
# Change the last element of numbers to 1
numbers[-1] = 1
# Get all the elements from numbers except the first two
numbers[2:]
# Check if 9 is an element of numbers
9 in numbers