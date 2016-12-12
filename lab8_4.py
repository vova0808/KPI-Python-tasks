
def make_sudoku(size):
    """Function that creates a sudoku matrix"""
    def mutate_list_1(lst, size):
        """Helper function for removing part of a list from the beginning and add it to the end."""
        count = 0
        while count < size:
            elem = lst[0]
            lst.remove(elem)
            lst.append(elem)
            count += 1
        return lst

    def mutate_list_2(lst):
        """Helper function for removing element from the beginning of a list and add it to the end."""
        elem = lst[0]
        lst.remove(elem)
        lst.append(elem)
        return lst

    count = 0
    matrix_length = size ** 2 # define a size of matrix
    matrix = [[] * matrix_length] # create an empty matrix
    matrix[0] = range(1, matrix_length + 1) # set a first row to a range from 1 to size ** 2
    while count < matrix_length - 1:
        l = matrix[count][:] # create a new list object that is a copy of previous row in a matrix
        if (count + 1)  % size == 0: # check if a row in inner square of a matrix
            l = matrix[count - (size-1)][:] # if it is, l set to the first row of previous square
            matrix.append(mutate_list_2(l))
        else:
            matrix.append(mutate_list_1(l, size)) # mutate l and add it to the matrix
        count += 1


    return matrix









print make_sudoku(3)