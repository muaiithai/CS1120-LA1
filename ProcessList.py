# importing the random library so we can generate random integers
import random


class ProcessList:
    # class' constructor, takes VALID number of rows and VALID number of columns as parameters
    def __init__(self, n_row, n_col):
        self.__n_row = n_row
        self.__n_col = n_col
        # A list comperhension is used to create the lists with passed dimensions and populate them with zeroes
        self.__rand_list = [[0 for i in range(self.__n_col)] for j in range(self.__n_row)]
        self.__adj_sum_list = [[0 for i in range(self.__n_col)] for j in range(self.__n_row)]

    # mutator for number of rows
    def set_n_row(self, val):
        self.__n_row = val

    # accessor for number of rows
    def get_n_row(self):
        return self.__n_row

    # mutator for number of columns
    def set_n_col(self, val):
        self.__n_col = val

    # accessor for number of columns
    def get_n_col(self):
        return self.__n_col

    # function to randomly fill the random list
    def randomlyFillList(self):
        # for loop that loops over the rand list's rows
        for i, row in enumerate(self.__rand_list):
            # for loop that loops over the elements of each row
            for j, element in enumerate(row):
                # setting the value in the element of the original rand list using its index to a random integer
                self.__rand_list[i][j] = random.randint(0, 15)

    # accessor for the rand list
    def get_rand_list(self):
        return self.__rand_list

    # function that computes the adjacent sum values for the computed list
    def computeListValues(self):
        # for loop that loops over the list's rows
        for i, row in enumerate(self.__adj_sum_list):
            # for loop that loops over the elements of each row
            for j, element in enumerate(row):
                # we test for edge cases to avoid index out of bounds error then add the valid adjacent values
                if not i == 0:
                    # adding the number to the left of the element
                    self.__adj_sum_list[i][j] += self.__rand_list[i - 1][j]
                if not i == (self.__n_row - 1):
                    # adding the number to the right of the element
                    self.__adj_sum_list[i][j] += self.__rand_list[i + 1][j]
                if not j == 0:
                    # adding the number above of the element
                    self.__adj_sum_list[i][j] += self.__rand_list[i][j - 1]
                if not j == (self.__n_col - 1):
                    # adding the number below of the element
                    self.__adj_sum_list[i][j] += self.__rand_list[i][j + 1]
                if (not i == 0) and (not j == 0):
                    # adding the number to the upper left of the element
                    self.__adj_sum_list[i][j] += self.__rand_list[i - 1][j - 1]
                if (not i == 0) and (not j == (self.__n_col - 1)):
                    # adding the number to the lower left of the element
                    self.__adj_sum_list[i][j] += self.__rand_list[i - 1][j + 1]
                if (not i == (self.__n_row - 1)) and (not j == 0):
                    # adding the number to the upper right of the element
                    self.__adj_sum_list[i][j] += self.__rand_list[i + 1][j - 1]
                if (not i == (self.__n_row - 1)) and (not j == (self.__n_col - 1)):
                    # adding the number to the lower right of the element
                    self.__adj_sum_list[i][j] += self.__rand_list[i + 1][j + 1]

    # accessor for the computed list
    def get_adj_sum_list(self):
        return self.__adj_sum_list

    # function that takes any list as a parameter and then prints it in a well-formatted way
    def printList(self, lista):
        # for loop that loops over the list's rows
        for row in lista:
            # for loop that loops over the elements of each row
            for element in row:
                # formatted printing of each element
                print(f'  {element:>2d}', end='')
            # breaking the line before proceeding to next row
            print()