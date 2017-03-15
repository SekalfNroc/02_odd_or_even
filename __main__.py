#!/usr/local/bin/python3

while True: # Broken on success
    try:
        number = int(input("Enter a number: \n> ")) 
        break
    except:
        pass

duple_remainder = number % 2
number_type = "even" if duple_remainder == 0 else "odd"

quadruple_remainder = number % 4
is_multiple_of_four = quadruple_remainder == 0

if is_multiple_of_four:
    print("You picked a multiple of four")
else:
    print("You picked an %s number." % number_type)

