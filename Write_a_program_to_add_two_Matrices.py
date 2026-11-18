def add_matrices(mat1,mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return "Matrices must have the same dimensions for addition"

    result= []
    for i in range(len(mat1[0])):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)

    return result

rows= int(input("Enter number of rows: "))
cols= int(input("Enter number of colums: "))

print("Enter matrix1: ")

matrix1 = []
for i in range(rows):
    row= list(map(int, input().split()))
    matrix1.append(row)

print("Enter matrix2: ")
matrix2= []
for i in range(rows):
    row= list(map(int, input().split()))
    matrix2.append(row)

result_matrix = add_matrices(matrix1,matrix2)

if isinstance(result_matrix,str):
    print(result_matrix)
else:
    print("Sum of matrices")
    for row in result_matrix:
        print(row)
