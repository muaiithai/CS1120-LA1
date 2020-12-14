#!/usr/bin/env python3

# CS1120 - Lab Assignment 01
# Author: Husain Abdelrahman
# Section: 540
# Submission date: 09/23/2020

# We import the ProcessList class from its file, set its keyword as PL for easier use
from ProcessList import ProcessList as PL


# LA1Main is a class that contains the body of our main
class LA1Main:
    def __init__(self):
        # take user input for rows using helper input function to make sure input is valid
        rows = self.input_valid_dim('row')
        # we loop over the input for columns until user inputs a value different from the rows value
        while 1:
            cols = self.input_valid_dim('col')
            if not cols == rows:
                break
            # prompt is displayed to user if they input the same number as for rows
            print('Number of columns is the same as number of rows!')
        # instance of ProcessList is created and valid values of rows and columns are passed to it
        process = PL(rows, cols)
        # we call randomlyFillList using the instance we created to fill its respective list
        process.randomlyFillList()
        # we call computeListValues using the instance we created to fill its respective list
        process.computeListValues()
        # header line to indicate which list is being printed is output
        print('\n\nInitial list with random numbers:\n')
        # ProcessList's printList function is called, and using an accessor, we pass the process instance's rand list
        process.printList(process.get_rand_list())
        # header line to indicate which list is being printed is output
        print('\n\nComputed list:\n')
        # ProcessList's printList function is called, using an accessor, we pass the process instance's computed list
        process.printList(process.get_adj_sum_list())

    # Helper function that validates the input values, takes a string as an argument to perform the related checks
    def input_valid_dim(self, rowsOrCols):
        # Do-While loop
        while 1:
            # different input prompt is displayed for the different input arguments
            if rowsOrCols == 'row':
                n = input('Enter number of rows in range [5, 20]:\n')
            elif rowsOrCols == 'col':
                n = input(f'Enter number of columns in range [5, 20]:\n'
                          f'This must be different from number of rows:\n')
            # try to cast the input as an int
            try:
                val = int(n)
                # if successful, we check if it's within the valid range
                if (5 <= val <= 20):
                    # if valid, the function returns it
                    return val
                # if not valid, the user is prompted that their input in invalid
                print('INVALID INPUT!')
            except ValueError:
                # an exception is thrown and a message is displayed to inform the user of their error
                print('Input must be an integer. Re-enter:')


main = LA1Main()