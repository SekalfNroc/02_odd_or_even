#!/usr/local/bin/python3

def input_number():
    while True: # Broken on success
        try:
            return int(input("Enter a number: \n> ")) 
        except:
            pass

number = input_number()

duple_remainder = number % 2
number_type = "even" if duple_remainder == 0 else "odd"

quadruple_remainder = number % 4
is_multiple_of_four = quadruple_remainder == 0

secondary_divisor = input_number() 
secondary_remainder = number % secondary_divisor
is_multiple_of_divisor = secondary_remainder == 0

if is_multiple_of_divisor:
    descriptor = "a multiple of the second number."
elif is_multiple_of_four:
    descriptor = "a multiple of four."
else:
    descriptor = "an %s number." % number_type

print("You picked %s" % descriptor)
