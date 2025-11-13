#!/usr/bin/env python3
# Created By: Christopher El-Murr
# Date: 11 08, 2025
# This program asks the user to input a number
# Then proceeds to calculate the sum of all the numbers leading up to it


def main():
    try:
        # define variables
        total = 0
        count = 0

        # try to convert string to an int
        number = int(input("Enter a positive integer: "))
        print("")

        # if number <= 0 print message and exit early
        if number <= 0:
            print("Please enter a positive number!")

        # Calculate the sum using a while loop
        while count <= number:
            print(f"{count} time through loop.")
            total += count
            count += 1

        print(f"The sum of the numbers from 0 to {number} is: {total}")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")
    except Exception as e:
        # catches any other unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
