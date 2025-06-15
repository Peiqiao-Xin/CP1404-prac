"""

  READ number_of_quick_picks
  WHILE number_of_quick_picks < 0 DO
    PRINT "That makes no sense!"
    READ number_of_quick_picks

  FOR i FROM 1 TO number_of_quick_picks DO
    quick_pick ← []
    FOR j FROM 1 TO NUMBERS_PER_LINE DO
      number ← RANDOM_INT(MINIMUM, MAXIMUM)
      WHILE number IN quick_pick DO
        number ← RANDOM_INT(MINIMUM, MAXIMUM)
      END WHILE
      APPEND number TO quick_pick
    END FOR
    SORT quick_pick
    PRINT quick_pick JOINED BY " "
"""

import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Quick picks program - choose sets of random numbers."""
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("That makes no sense!")
        number_of_quick_picks = int(input("How many quick picks? "))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        # the following uses a generator expression (like a list comprehension)
        # to format each number in quick_pick in the same way
        # this is then turned into a single string with the join method
        print(" ".join(f"{number:2}" for number in quick_pick))


main()