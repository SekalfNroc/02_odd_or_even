#!/usr/local/bin/python3

while True: # Broken on success
    try:
        number = int(input("Enter a number: \n> ")) 
        break
    except:
        pass

duple_remainder = number % 2
number_type = "even" if duple_remainder == 0 else "odd"

