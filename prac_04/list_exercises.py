"""

  numbers ← []
  FOR i FROM 1 TO 5 DO
    READ number
    APPEND number TO numbers
  END FOR
  PRINT "First number is", numbers[0]
  PRINT "Last number is", numbers[-1]
  PRINT "Smallest number is", MIN(numbers)
  PRINT "Largest number is", MAX(numbers)
  PRINT "Average is", SUM(numbers) / LENGTH(numbers)

  usernames ← ['jimbo', 'giltson98', …, 'bob']
  READ username
  IF username IN usernames THEN
    PRINT "Access granted"
  ELSE
    PRINT "Access denied"
  END IF
"""

# 1. Numbers stuff
numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

print("The first number is", numbers[0])
print("The last number is", numbers[-1])
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))
print("The average of the numbers is", sum(numbers) / len(numbers))

# 2. Woefully inadequate security checker...
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
             'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command',
             'ExecState', 'InteractiveConsole', 'InterpreterInterface',
             'StartServer', 'bob']
username = input("Enter username:")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")