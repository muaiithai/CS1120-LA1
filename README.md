# CS1120-LA1
pythonic-minesweeper

This is a python application that simulates a portion of the game Minesweeper using the details specified below. 
In the game, a square minefield exists with “mines” located at random cells of the minefield. 
The cells immediately surrounding the minefields each have a number indicating how many adjacent locations are mines. 

This python code creates a two-dimensional list using input obtained from the user. 
The number of rows must not be equal to the number of columns (both of these will be user input). 
The dimensions (rows and columns) of the list should be in the range [5, 20] inclusive. 
Create a second identical list. Your program should fill the first list with random integers in the range [0, 15] inclusive. 
Then, starting at the upper left-hand corner of your first list, for each cell, 
compute the sum of all adjacent cells and assign the result to the corresponding cell in the second list. 
The values in the first list should not be overwritten once they have been determined randomly. 
This program should then print out the values in the first and second lists.
