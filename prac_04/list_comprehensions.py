"""


  names ← ["Bob", "Angel", "Jimi", "Alan", "Ada"]
  full_names ← ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]
  almost_numbers ← ['0', '10', '21', '3', '-7', '88', '9']

  first_initials ← []
  FOR each name IN names DO
    APPEND first character of name TO first_initials
  END FOR
  PRINT first_initials

  first_initials ← [first character of name FOR name IN names]
  PRINT first_initials

  full_initials ← [first letter of first word + first letter of second word FOR name IN full_names]
  PRINT full_initials

  a_names ← [name FOR name IN names IF name starts with 'A']
  PRINT a_names

  lowercase_full_names ← [lowercase(name) FOR name IN full_names]
  PRINT lowercase_full_names

  numbers ← [integer(value) FOR value IN almost_numbers]
  PRINT numbers

  big_numbers ← [n FOR n IN numbers IF n > 9]
  PRINT big_numbers
"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing",
              "Ada Lovelace"]

# for loop that creates a new list containing the first letter of each name
first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

# list comprehension that does the same thing as the loop above
first_initials = [name[0] for name in names]
print(first_initials)

# list comprehension that creates a list containing the initials
# splits each name and adds the first letters of each part to a string
full_initials = [name.split()[0][0] + name.split()[1][0] for name in
                 full_names]
print(full_initials)

# one more example, using filtering to select only the names that start with A
a_names = [name for name in names if name.startswith('A')]
print(a_names)

# TODO: use a list comprehension to create a list of all of the full_names
# in lowercase format
lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
# TODO: use a list comprehension to create a list of integers
# from the above list of strings
numbers = [int(almost_number) for almost_number in almost_numbers]
print(numbers)

# TODO: use a list comprehension to create a list of only the numbers that are
# greater than 9 from the numbers (not strings) you just created
big_numbers = [number for number in numbers if number > 9]
print(big_numbers)