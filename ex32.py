the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#1, 2, 3, 4, 5
for number in the_count:
    print(f"This is count {number}")

#apples, oranges, pears, apricots
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

#1, pennies, 2, dimes, 3, quarters
for i in change:
    print(f"I got {i}")

elements = []


"""range(first, last), range function only does numbers
from the first to the last, not including the last.

"""
#0, 1, 2, 3, 4, 5,  from 0 to 6, not including 6
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)

#0, 1, 2, 3, 4, 5
for i in elements:
    print(f"Element was: {i}")