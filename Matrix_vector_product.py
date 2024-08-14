



def display_matrix_columns(matrix):
    for row in matrix:
        col_message = ""
        #print(row)
        for col in row:
            col_message += str(col) + "\t"
        print(col_message)

def check_vector_compatibility(matrix,vector):
    #check for properly formatted matrix:
    for row in matrix:
        row_len = len(matrix[0])
        if len(row) != row_len:
            print("Error! Uneven Matrix")
    #make sure that vector has as many entries as the matrix does columns
    if len(matrix[0]) == len(vector):
        return True
    else:
        return False

def multiply_matrix_vector(matrix, vector):
    compatible = check_vector_compatibility(matrix, vector)
    new_vector = []
    if compatible:
        for row in matrix:
            row_sum = 0
            for i, col in enumerate(row):
                #print("multiplying", col, "*", vector[i])
                row_sum += col * vector[i]
                #print("adding", col * vector[i], "to row_sum:", row_sum)
            #print(row_sum)
            new_vector.append(row_sum)
    return new_vector

matrix_a = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]]
matrix = matrix_a
vector = [10,100,1000,1]

print(multiply_matrix_vector(matrix, vector))