#!/usr/bin/env python3

# Created by: Ethan Gravelle
# Created on: May 12, 2020
# This program calculates the sum of all integers of a positive number.

def main():
    # This function calculates the sum of all integers of a positive number.

    # this is to keep track of hw many times you go through the loop.
    loop_counter = 1

    # this is the sum of all numbers.
    total = 1

    # input
    print("\n", end="")
    integer = input("Enter a positive integer: ")
    print("")
    # process & output
    try:
        positive_integer = int(integer)
        if positive_integer >= 0:
            while loop_counter <= positive_integer:
                total = total * loop_counter
                loop_counter = loop_counter + 1

            print("The sum of all positive numbers from 1 to {0} is {1}."
                  .format(positive_integer, total))
        else:
            print("Sorry {0} is not a valid input.".format(positive_integer))
    except Exception:
        print("{0} is not a valid input.".format(integer))

    print("\nDone.")


if __name__ == "__main__":
    main()
